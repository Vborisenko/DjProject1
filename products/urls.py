from django.urls import path
from .views import (product_create_view,
                    render_data,
                    delete_product_view,
                    product_detail_view,
                    product_list_view,
                    )

app_name = "products"               # namespace
urlpatterns = [
    path('create/', product_create_view, name="create-product"),
    path('render', render_data, name="render-product"),
    path('delete/<int:id>/', delete_product_view, name="delete-product"),
    path('<int:id>/', product_detail_view, name="product-details"),  # Dynamic URL Routing
    path('', product_list_view, name="product-list"),  # Dynamic URL Routing
]
