"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import pages.views
import products.views
import workers.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pages.views.home_view, name='home'),
    path('products/<int:id_product>/', products.views.product_detail_view),   # Dynamic URL Routing
    path('contact/', pages.views.contact_view),
    path('me/', pages.views.aboutme_view),
    path('create_worker/', workers.views.worker_create_view),
    path('create_product/', products.views.product_create_view),
    path('render_product/', products.views.render_data, name='product'),
]
