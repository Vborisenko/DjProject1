from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    print("user:", request.user)
    # return HttpResponse("<title>Homepage</title>"# string of HTML code
    return render(request, "home.html", {})


def aboutme_view(request, *args, **kwargs):
    print("user:", request.user)
    return render(request, "me.html", {})


def contact_view(request, *args, **kwargs):
    print("user:", request.user)
    return render(request, "contact.html", {})

