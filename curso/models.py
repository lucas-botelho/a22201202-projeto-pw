from django.db import models

class Curso(models.Model):
    name = models.CharField(max_length=100)
    objectives = models.TextField()
    presentation = models.TextField()
    competences = models.TextField()

    def __str__(self):
        return self.name

class AreaCientifica(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Disciplina(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    semester = models.CharField(max_length=100)
    ects = models.IntegerField()
    curricularIUnitReadableCode = models.CharField(max_length=100)
    scientificArea = models.ForeignKey(AreaCientifica, on_delete=models.CASCADE)
    course = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Projeto(models.Model):
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    tecnologias_usadas = models.TextField()
    imagem = models.ImageField(upload_to='projeto_imagens/', null=True, blank=True)
    video_link = models.URLField(blank=True)
    github_repo_link = models.URLField(blank=True)
    language = models.ForeignKey('LinguagemDeProgramacao', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Projeto para {self.disciplina.name}"


class LinguagemDeProgramacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=100)
    disciplinas = models.ManyToManyField('Disciplina', related_name='docentes')

    def __str__(self):
        return self.nome
