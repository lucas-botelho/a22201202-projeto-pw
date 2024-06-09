from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.article_list, name='index'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('article/<int:article_id>/edit/', views.edit_article, name='edit_article'),
    path('article/create/', views.create_article, name='create_article'),
    path('article/delete/<int:article_id>/', views.delete_article, name='delete_article'),
    path('author/<int:author_id>/edit/', views.edit_author, name='edit_author'),
    path('author/create/', views.create_author, name='create_author'),
    path('author/delete/<int:author_id>/', views.delete_author, name='delete_author'),
    path('comment/create/<int:article_id>/', views.create_comment, name='create_comment'),
]
