from django.shortcuts import render
from .models import Mentor

def db_Mentor(request):
    mentor = Mentor.objects.all()
    return render(request, 'Mentor/Mentor.html', {'mentors' : mentor})