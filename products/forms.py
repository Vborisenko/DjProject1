from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {
            'title',
            'description',
            'price',
            'feature',
        }


class RawProductForm(forms.Form):
    title       = forms.CharField(required=True, label='',
                                  widget=forms.TextInput(
                                      attrs={
                                          "placeholder": "Your title"
                                      }))
    description  = forms.CharField(required=False,
                                   label='',
                                   widget=forms.Textarea(
                                       attrs={
                                           "class": "home-page",
                                           "rows": 2,
                                           "id": "desc_textarea",
                                           "cols": 22,
                                           "placeholder": "Your description"
                                       }))
    price       = forms.DecimalField(initial=199.99,
                                     label='')