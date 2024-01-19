from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! You can visit <a href='/rango/about/'>the about page</a>.")

def about(request):
    return HttpResponse("Rango says here is the about page. You can go back to <a href='/rango/'>the home page</a>.")