from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Ator(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    nacionalidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='filme_images/', blank=True, null=True)
    ano_lancamento = models.IntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    atores = models.ManyToManyField(Ator)

    def __str__(self):
        return self.titulo
