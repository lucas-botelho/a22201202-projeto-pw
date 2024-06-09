from django.urls import path
from . import views

app_name = 'biblioteca'


urlpatterns = [
    path('', views.index_view, name="index"),
    path('autor/<int:autor_id>/', views.autor_view, name="autor"),
    path('livro/<int:livro_id>/', views.livro_view, name="livro"),
    path('generos/', views.generos_view, name="generos"),
    path('genero/<str:genero>', views.genero_view, name="genero"),
    path('autor/novo', views.novo_autor_view,name="novo_autor"),
    path('autor/<int:autor_id>/edita', views.edita_autor_view,name="edita_autor"),
    path('autor/<int:autor_id>/apaga', views.apaga_autor_view,name="apaga_autor"),
    path('autor/<int:autor_id>/novo-livro/', views.novo_livro_view,name="novo_livro"),
]