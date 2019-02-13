from django.urls import path
from .import views

urlpatterns = [
    path('Mentee', views.db_Mentee, name='Mentee'),
]