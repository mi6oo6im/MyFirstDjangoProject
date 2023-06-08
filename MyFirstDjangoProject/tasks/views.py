from django.http import HttpResponse
from django.shortcuts import render
from MyFirstDjangoProject.tasks.models import Task


# Create your views here.


def index(request):
    return HttpResponse("It works!")


def all_tasks(request):
    result = Task.objects.all()
    context = {
        "title": "Today's tasks",
        "tasks": result,
    }
    return render(request, "tasks/all_tasks.html", context)
