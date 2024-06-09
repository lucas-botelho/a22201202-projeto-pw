from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    formed_in = models.IntegerField()
    photo = models.ImageField(upload_to='banda_imagens/', blank=True, null=True)
    info = models.TextField()
    nacionality = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    cover = models.ImageField(upload_to='banda_imagens/', blank=True, null=True)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    spotify_link = models.URLField(blank=True, null=True)
    duration = models.CharField(max_length=100)
    letra = models.TextField(default='', null=True, blank=True)
    biografia = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return self.title

