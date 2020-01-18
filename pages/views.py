from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home_view(request, *args, **kwargs):
    print("user:", request.user)
    # return HttpResponse("<title>Homepage</title>"# string of HTML code
    return render(request, "home.html", {})


def aboutme_view(request, *args, **kwargs):
    # print("user:", request.user)
    my_context = {
        'my_name': '<h1>vitali barysenka</h1>',
        'title': 'django web-site',
        "my_text": "This page is about me",
        "my_number": 375291865630,
        "my_skills": ['Python/Django', 'HTML/CSS', 'Git', 'Linux(bush)', 'OOP', 'SQL']
    }
    return render(request, "me.html", my_context)


def contact_view(request, *args, **kwargs):
    print("user:", request.user)
    return render(request, "contact.html", {})

