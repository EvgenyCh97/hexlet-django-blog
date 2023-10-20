from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'articles/index.html', context={
        'app_name': 'hexlet_django_blog.articles'
    })
