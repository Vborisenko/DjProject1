from django.shortcuts import render
from django.views.generic import (CreateView,
                                  DetailView,
                                  ListView)
from .models import Article
# Create your views here.


class ArticleView(ListView):
    template_name   = 'articles/article_list.html'
    queryset        = Article.objects.all()  # blog/<modelname>_list.html
