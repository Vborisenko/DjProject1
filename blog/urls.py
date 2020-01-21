from django.urls import path
from .views import (ArticleView)

app_name = "articles"               # namespace
urlpatterns = [
    path('', ArticleView.as_view(), name='article-list'),

]