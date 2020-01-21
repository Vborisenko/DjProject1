from django.shortcuts import render, get_object_or_404
from django.views.generic import (CreateView,
                                  DetailView,
                                  ListView,)
from .models import Article
# Create your views here.


class ArticleView(ListView):
    template_name   = 'articles/article_list.html'
    queryset        = Article.objects.all()  # blog/<modelname>_list.html


class ArticleDetailView(DetailView):
    template_name   = 'articles/article_detail.html'
    queryset        = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)