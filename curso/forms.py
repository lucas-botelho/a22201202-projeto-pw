from django import forms
from .models import Curso, AreaCientifica, Disciplina, Projeto, LinguagemDeProgramacao, Docente

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['name', 'objectives', 'presentation', 'competences']

class AreaCientificaForm(forms.ModelForm):
    class Meta:
        model = AreaCientifica
        fields = ['name']

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = [
            'name', 'year', 'semester', 'ects', 
            'curricularIUnitReadableCode', 'scientificArea', 'course'
        ]

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = [
            'disciplina', 'descricao', 'conceitos_aplicados', 
            'tecnologias_usadas', 'imagem', 'video_link', 
            'github_repo_link', 'language'
        ]

class LinguagemDeProgramacaoForm(forms.ModelForm):
    class Meta:
        model = LinguagemDeProgramacao
        fields = ['nome']

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nome', 'disciplinas']
