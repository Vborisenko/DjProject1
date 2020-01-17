from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    print("user:", request.user)
    # return HttpResponse("<title>Homepage</title>"# string of HTML code
    return render(request, "home.html", {})


def aboutme_view(request, *args, **kwargs):
    print("user:", request.user)
    my_context = {
        'my_name' : 'Vitali',
        "my_text": "This is about me",
        "my_number": 777,
        "my_list": ['Vitali', 'Ighor', 'Max', '400', '400', '500']
    }

    return render(request, "me.html", my_context)


def contact_view(request, *args, **kwargs):
    print("user:", request.user)
    return render(request, "contact.html", {})

