from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def ryan(request):
    return HttpResponse("Hello, Ryan!")

def behnaz(request):
    return HttpResponse("Hello, Behnaz!")

def greet(request, name):
    return render(request, "hello/greet.html", {"name": name.capitalize()})