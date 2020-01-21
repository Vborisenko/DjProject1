from django.urls import path
from .views import (ArticleView,
                    ArticleDetailView,
                    ArticleCreateView,
                    ArticleUpdateView,)

app_name = "articles"               # namespace
urlpatterns = [
    path('', ArticleView.as_view(), name='article-list'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),   # <int:pk> is default. If you want to change
    path('create/', ArticleCreateView.as_view(), name='article-create'),   # you should to override method in ViewsClass
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
]