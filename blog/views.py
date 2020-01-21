from django.shortcuts import render, get_object_or_404
from django.views.generic import (CreateView,
                                  DetailView,
                                  ListView,
                                  UpdateView,)
from .forms import ArticleModelForms
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


class ArticleCreateView(CreateView):
    form_class            = ArticleModelForms
    template_name   = 'articles/article_create.html'
    queryset        = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    form_class            = ArticleModelForms
    template_name   = 'articles/article_create.html'
    queryset        = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)