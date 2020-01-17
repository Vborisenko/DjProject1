from django.shortcuts import render
from .models import Product


# Create your views here.

def product_detail_view(request):
    try:
        obj = Product.objects.get(id=1)
    except Product.DoesNotExist:
        obj = None
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price,
    # }
    context = {
        'object': obj
    }
    # if context['description'] is None:
    #     print("Soon")
    # else:
    #     print("description:", context['description'])
    return render(request, "products/product_details.html", context)

