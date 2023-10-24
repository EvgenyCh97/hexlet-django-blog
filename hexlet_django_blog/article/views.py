from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class IndexView(View):

    def get(self, request, **kwargs):
        return render(request, 'articles/index.html', context={
            'app_name': 'hexlet_django_blog.articles'
        })
