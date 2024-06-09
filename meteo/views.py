from django.http import JsonResponse
import requests
from django.shortcuts import render
from datetime import date

# Endpoint para obter a lista de cidades
CITIES_URL = 'https://api.ipma.pt/open-data/distrits-islands.json'
# Endpoint para obter a previsão meteorológica de uma cidade
FORECAST_URL = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{}.json'
# Endpoint para obter a descrição do tempo
WEATHER_TYPES_URL = 'https://api.ipma.pt/open-data/weather-type-classe.json'



def previsao(request):
    response = requests.get(CITIES_URL)
    cities = response.json().get('data', [])
    
    return render(request, 'meteo/previsao.html', {'cities': cities})

def previsao_cidade(request, city_id):
    response = requests.get(FORECAST_URL.format(city_id))
    weathertypesResponse = requests.get(WEATHER_TYPES_URL)
    weathertypes = weathertypesResponse.json()

    if response.status_code == 200:
        dic_dados = response.json()
        hoje = date.today().strftime('%Y-%m-%d')
        previsoes_proximos_dias = []
        for item in dic_dados['data']:
            if item['forecastDate'] >= hoje and len(previsoes_proximos_dias) < 5:
                descricao = ''  
                for weather in weathertypes['data']:
                    if item['idWeatherType'] == weather['idWeatherType']:
                        descricao =  weather['descWeatherTypePT']
                        break
                id_weather_type = "%02d" % item['idWeatherType']
                weather_type_url = '/static/meteo/w_ic_d_' + str(id_weather_type) + 'anim.svg'
                
                prev = {
                    'day': item,
                    'weather_type_url': weather_type_url,
                    'weatherDescription': descricao
                }

                previsoes_proximos_dias.append(prev)

    return JsonResponse({'forecast': previsoes_proximos_dias})   

def previsao_lisboa(request):
    global_id_lisboa = 1110600 
    
    response = requests.get(FORECAST_URL.format(global_id_lisboa))
    if response.status_code == 200:
        dic_dados = response.json()
        hoje = date.today().strftime('%Y-%m-%d')
        previsao_hoje = None
        for item in dic_dados['data']:
            if item['forecastDate'] == hoje:
                previsao_hoje = item
                break      

        id_weather_type = "%02d" % previsao_hoje['idWeatherType']
        weather_type_url = '/static/meteo/w_ic_d_' + str(id_weather_type) + 'anim.svg'

        weathertypes = requests.get(WEATHER_TYPES_URL)
        descricao = ''
        responsejson = weathertypes.json()
        for weather in responsejson['data']:
            if weather['idWeatherType'] == previsao_hoje['idWeatherType']:
                descricao = weather['descWeatherTypePT']
                break

        contexto = {
            'previsao': previsao_hoje,
            'weather_type_url': weather_type_url,
            'descricao': descricao
        }
        return render(request, 'meteo/previsao_lisboa.html', contexto)
    else:
        return render(request, 'meteo/previsao_lisboa.html', {'erro': 'Não foi possível obter os dados da API.'})
    

def lista_cidades(request):
    response = requests.get(CITIES_URL)
    cidades = response.json().get('data', [])
    return JsonResponse({'cidades': cidades})

def tempo_cidade(request, city_id):
    response = requests.get(FORECAST_URL.format(city_id))
    if response.status_code == 200:
        dic_dados = response.json()
        hoje = date.today().strftime('%Y-%m-%d')
        previsao_hoje = None
        for item in dic_dados['data']:
            if item['forecastDate'] == hoje:
                previsao_hoje = item
                break      

    nomecidade = ''
    response = requests.get(CITIES_URL)
    cidades = response.json().get('data', [])
    for cidade in cidades:
        if cidade['globalIdLocal'] == city_id:
            nomecidade = cidade['local']
            break

    apiresponse = dict()

    apiresponse['cidade'] = nomecidade
    apiresponse['temperatura_min'] = previsao_hoje['tMin']
    apiresponse['temperatura_max'] = previsao_hoje['tMax']
    id_weather_type = "%02d" % previsao_hoje['idWeatherType']
    apiresponse['weather_type_url'] = f'https://{request.get_host()}/static/meteo/w_ic_d_' + str(id_weather_type) + 'anim.svg'
    apiresponse['data'] = previsao_hoje['forecastDate']
    apiresponse['precipitaProb'] = previsao_hoje['precipitaProb']

    weathertypes = requests.get(WEATHER_TYPES_URL)

    responsejson = weathertypes.json()
    for weather in responsejson['data']:
        if weather['idWeatherType'] == previsao_hoje['idWeatherType']:
            apiresponse['descricao'] =  weather['descWeatherTypePT']
            break


    return JsonResponse({'forecast': apiresponse})