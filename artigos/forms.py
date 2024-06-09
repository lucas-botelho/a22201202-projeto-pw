from django import forms
from .models import Article, Author, Comment

class ArticleForm(forms.ModelForm):
    
    article_id = forms.IntegerField(widget=forms.HiddenInput(), required=False, initial=Article.objects.latest('article_id').article_id+1)  
    class Meta:
        model = Article
        fields = ['article_id', 'title', 'content']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']