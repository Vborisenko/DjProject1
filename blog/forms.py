from django import forms
from .models import Article


class ArticleModelForms(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active',
        ]