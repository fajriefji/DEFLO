from django.urls import path
from .import views

urlpatterns = [
    path('Blog', views.db_blog, name='Blog'),
    path('new-post', views.input_post, name='new-post')
]