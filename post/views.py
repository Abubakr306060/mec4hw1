from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("hello world")

def goodbye(request):
    return HttpResponse("good bye")

def about(request):
    return HttpResponse("О нас")

def gobal(request):
    return HttpResponse("Главная страница")

from datetime import datetime

def time(request):
    time = datetime.now()
    return HttpResponse(time)