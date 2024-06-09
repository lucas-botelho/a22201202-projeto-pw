from django import forms
from .models import Autor, Livro

class AutorForm(forms.ModelForm):
  class Meta:
    model = Autor
    fields = '__all__'

    widgets = {
      'nome': forms.TextInput(attrs={
          'placeholder':'Nome completo',
      })
    }    

class LivroForm(forms.ModelForm):
  class Meta:
    model = Livro
    fields = '__all__'
    
    labels = {
      'titulo': 'Título',
      'ano_publicacao': 'Ano de Publicação',
    }
    
    help_texts = {
      'ano_publicacao': 'verifique o ano de publicação', 
    }
