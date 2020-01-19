from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(required=True,
                            label='',
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "My title"
                                }))
    description = forms.CharField(required=False,
                                  label='',
                                  widget=forms.Textarea(
                                      attrs={
                                          "class": "home-page",
                                          "rows": 2,
                                          "id": "desc_textarea",
                                          "cols": 22,
                                          "placeholder": "Your description"
                                      }))
    price = forms.DecimalField(initial=199.99,
                               label='', max_digits=6)

    class Meta:
        model = Product
        fields = {
            'title',
            'description',
            'price',
            'feature',
        }

    # Overriding some default functions
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "lol" in title:
            raise forms.ValidationError("Your title shoul contain the word 'lol'!")
        return title


class RawProductForm(forms.Form):
    title = forms.CharField(required=True, label='',
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "Your title"
                                }))
    description = forms.CharField(required=False,
                                  label='',
                                  widget=forms.Textarea(
                                      attrs={
                                          "class": "home-page",
                                          "rows": 2,
                                          "id": "desc_textarea",
                                          "cols": 22,
                                          "placeholder": "Your description"
                                      }))
    price = forms.DecimalField(initial=199.99,
                               label='')
