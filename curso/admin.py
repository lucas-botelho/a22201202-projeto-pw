from django.contrib import admin
from .models import Curso, AreaCientifica, Disciplina, Projeto, LinguagemDeProgramacao, Docente

admin.site.register(Curso)
admin.site.register(AreaCientifica)
admin.site.register(Disciplina)
admin.site.register(Projeto)
admin.site.register(LinguagemDeProgramacao)
admin.site.register(Docente)
