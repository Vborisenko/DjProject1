from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    print("user:", request.user)
    return HttpResponse("<title>Homepage</title>"
                        "<h1>Hello World</h1>")  # string of HTML code


def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Vitali Barysenka's web-site</h1>")
    return render(request, "home.html")

def contact_view(request, *args, **kwargs):
    print("user:", request.user)
    return HttpResponse("<h1>Vitali Barysenka's Contact Page</h1>")


def social_view(request, *args, **kwargs):
    print("user:", request.user)
    return HttpResponse("<h1>Vitali Barysenka's web-site</h1>")