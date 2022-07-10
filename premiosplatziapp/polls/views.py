from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return new_func()

def new_func():
    return HttpResponse("Hello World")
