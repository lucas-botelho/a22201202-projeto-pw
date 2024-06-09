from django.shortcuts import render, redirect
from .models import Article, Comment, Author
from .forms import ArticleForm, AuthorForm, CommentForm
from django.contrib.auth.decorators import login_required

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'artigos/article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article_id=article_id)
    return render(request, 'artigos/article_detail.html', {'article': article, 'comments': comments})

@login_required
def edit_article(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('artigos:article_detail', article_id=article.id)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'artigos/edit_article.html', {'form': form})

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            author, created = Author.objects.get_or_create(
                name=request.user.first_name,
                defaults={'bio': ''}
            )
            article.author = author
            article.save()
            return redirect('artigos:article_detail', article_id=article.id)
    else:
        form = ArticleForm()
        form.base_fields['article_id'].initial = Article.objects.latest('article_id').article_id+1
    return render(request, 'artigos/create_article.html', {'form': form})


@login_required
def delete_article(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('artigos:index', article_id=article.id)
    
    return render(request, 'artigos/confirm_delete.html', {'article': article})

@login_required
def edit_author(request, author_id):
    author = Author.objects.get(id=author_id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('artigos:author_detail', author_id=author.id)
    else:
        form = AuthorForm(instance=author)
    return render(request, 'artigos/edit_author.html', {'form': form})

@login_required
def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect('author_detail', author_id=author.id)
    else:
        form = AuthorForm()
    return render(request, 'artigos/create_author.html', {'form': form})

@login_required
def delete_author(request, author_id):
    author = Author.objects.get(id=author_id)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'artigos/confirm_delete.html', {'author': author})


@login_required
def create_comment(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            article = Article.objects.get(id=article_id)
            comment.author = Author.objects.get(id=article.author.id)
            comment.article = article
            comment.save()
            return redirect('artigos:article_detail', article_id=article_id)
    else:
        form = CommentForm()
        
    return render(request, 'artigos/create_comment.html', {'form': form})