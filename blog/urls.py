from django.urls import path
from .views import (ArticleView,
                    ArticleDetailView,)

app_name = "articles"               # namespace
urlpatterns = [
    path('', ArticleView.as_view(), name='article-list'),
    path('<int:id>', ArticleDetailView.as_view(), name='article-detail'),   # <int:pk> is default. If you want to change
    path('<int:id>', ArticleDetailView.as_view(), name='article-detail'),   # you should to override method in ViewsClass
    # path('<int:id>', ArticleDetailView.as_view(), name='article-detail'),
]