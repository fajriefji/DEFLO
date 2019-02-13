from django.urls import path
from .import views

urlpatterns = [
    path('Mentor', views.db_Mentor, name='Mentor'),
]