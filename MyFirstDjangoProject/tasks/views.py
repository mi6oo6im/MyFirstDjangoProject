from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("It works!")


def all_tasks(request):
    return HttpResponse("It works!")
