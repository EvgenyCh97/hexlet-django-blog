from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class Index(View):

    def get(self, request, tags='python', article_id=42):
        return render(request, 'articles/index.html', context={
            'tags': tags,
            'article_id': article_id,
        })
