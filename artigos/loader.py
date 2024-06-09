from .models import *
import json

Author.objects.all().delete() 
Article.objects.all().delete() 
Comment.objects.all().delete() 

with open('artigos/json/authors.json') as f:
    autores = json.load(f)
    for autor in autores:
        Author.objects.create(
            name=autor['name'],
            bio=autor['bio'],
        )


with open('artigos/json/articles.json') as f:
    artigos = json.load(f)
    for artigo in artigos:
        author = Author.objects.get(name=artigo['author'])
        Article.objects.create(
           title=artigo['title'],
           content=artigo['content'],
           author =author,
           article_id=artigo['article_id']
        )


with open('artigos/json/comments.json') as f:
    comentarios = json.load(f)
    for comentario in comentarios:
        autor = Author.objects.get(name=comentario['author'])
        artigo = Article.objects.get(article_id=comentario['article_id'])

        Comment.objects.create(
            content=comentario['content'],
            author=autor,
            article=artigo
        )
