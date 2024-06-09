from django.shortcuts import render
from .models import Filme, Genero, Ator

def lista_filmes(request):
    generos = Genero.objects.all()
    filmes_por_genero = {}
    for genero in generos:
        filmes_por_genero[genero] = Filme.objects.filter(genero=genero)

    return render(request, 'filmes/lista_filmes.html', {'filmes_por_genero': filmes_por_genero})


def filme_detail(request, filme_id):
    filme = Filme.objects.get(id=filme_id)
    atores = Ator.objects.filter(filme=filme)
    return render(request, 'filmes/filme_detail.html', {'filme': filme, 'atores': atores})