from django.http import HttpResponse
from django.shortcuts import render


def index(request):  #HttpRequests
    return HttpResponse('Страница приложения women.')


def categories(request):  #HttpRequests
    return HttpResponse('<h1>Статьи по категориям.</h1>')