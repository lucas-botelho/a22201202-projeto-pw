from django import forms
from .models import *

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'album', 'spotify_link', 'duration', 'letra', 'biografia']
        help_texts = {
            'title': 'Insira o título da música.',
            'album': 'Selecione o álbum ao qual a música pertence.',
            'spotify_link': 'Insira o link do Spotify da música (opcional).',
            'duration': 'Insira a duração da música.',
            'letra': 'Insira a letra da música (opcional).',
            'biografia': 'Insira uma biografia curta da música (opcional).'
        }
        
class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ['name', 'genre', 'formed_in', 'photo', 'info', 'nacionality']
        help_texts = {
            'name': 'Insira o nome da banda.',
            'genre': 'Insira o gênero musical da banda.',
            'formed_in': 'Insira o ano de formação da banda.',
            'photo': 'Selecione uma foto da banda.',
            'info': 'Insira informações adicionais sobre a banda.',
            'nacionality': 'Insira a nacionalidade da banda.'
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'release_year', 'cover', 'band']
        help_texts = {
            'title': 'Insira o título do álbum.',
            'release_year': 'Insira o ano de lançamento do álbum.',
            'cover': 'Selecione a capa do álbum.',
            'band': 'Selecione a banda associada ao álbum.'
        }
