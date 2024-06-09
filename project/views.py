from django.http import JsonResponse
from django.shortcuts import render

from artigos.models import *

from django.conf import settings
INSTALLED_APPS = settings.INSTALLED_APPS

def index(request):
    return render(request, 'project/index.html')


def mebyme(request):
    return render(request, 'project/mebyme.html')

def sobre(request):
    return render(request, 'project/sobre.html')