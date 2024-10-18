from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")

def index_es(request):
    return render(request, "index_es.html")

def contact(request):
    return render(request, "contact.html")

def contact_es(request):
    return render(request, "contact_es.html")

def gallery(request):
    return render(request, "gallery.html")

def gallery_es(request):
    return render(request, "gallery_es.html")

def about(request):
    return render(request, "about.html")

def about_es(request):
    return render(request, "about_es.html")
