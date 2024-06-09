"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='allapps'),
    path('mebyme', views.mebyme, name='mebyme'),
    path('sobre', views.sobre, name='sobre'),
    path('admin/', admin.site.urls),
    path('noobsite/', include('noobsite.urls')),
    path('pwsite/', include('pwsite.urls')),
    path('bandas/', include('bandas.urls')),
    path('artigos/', include('artigos.urls')),
    path('filmes/', include('filmes.urls')),
    path('curso/', include('curso.urls')),
    path('autenticacao/', include('autenticacao.urls')),
    path('biblioteca/', include('biblioteca.urls')),
    path('meteo/', include('meteo.urls')),
]
