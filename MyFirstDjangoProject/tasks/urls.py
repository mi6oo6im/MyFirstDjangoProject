from django.urls import path

from .views import index, all_tasks

urlpatterns = [
    path('', index),
    path('all/', all_tasks)
]
