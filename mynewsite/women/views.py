from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):  # HttpRequests
    return HttpResponse('Страница приложения women.')


def categories(request, cat):  # HttpRequests
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{cat}</p>')


def archive(request, year):  # HttpRequests
    if int(year) > 2022:
        return redirect('home', permanent=False)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def page_not_found(request, exception):  # HttpRequests
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
