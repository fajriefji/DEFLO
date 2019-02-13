from django.urls import path
from .import views

urlpatterns = [
    path('Author', views.Author, name='Author'),
]