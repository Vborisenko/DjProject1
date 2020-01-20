from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.


#   Pure Django form
# def product_create_view(request):
#     raw_form = RawProductForm()
#     if request.method == "POST":
#         raw_form = RawProductForm(request.POST)
#         if raw_form.is_valid():
#             print(raw_form.cleaned_data)
#             Product.objects.create(**raw_form.cleaned_data)
#     context = {
#         "form": raw_form
#     }
#     return render(request, "products/product_create.html", context)


# Row html form without form in Django
# def product_create_view(request):
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         my_new_description = request.POST.get('description)
#         my_new_price = request.POST.get('price')
#         print('title:', my_new_title)
#         print('price:', my_new_price)
#         Product.objects.create(title = my_new_title, description = my_new_description, price = my_new_price)
#     return render(request, "products/product_create.html", {})


# Django form for templates
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def render_data(request):
    form = ProductForm()
    if request.method == "POST":
        id_product = request.POST.get('id_product')
        try:
            obj = Product.objects.get(id=id_product)
            print("изъяли из бд:", obj.title)
        except Product.DoesNotExist:
            obj = None
        form = ProductForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return render(request, "products/render.html", context)


def product_detail_view(request, id_product):

    obj = get_object_or_404(Product, id=id_product)
    # try:
    #     obj = Product.objects.get(id=id_product)
    # except Product.DoesNotExist:
    #     raise Http404
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price,
    # }
    context = {
        'object': obj
    }
    return render(request, "products/product_details.html", context)


def delete_product_view(request, id_p):
    obj = get_object_or_404(Product, id = id_p)
    # POST request
    if request.method == "POST":
        # confirming delete
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)