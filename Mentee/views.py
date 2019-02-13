from django.shortcuts import render
from .models import Mentee


def db_Mentee(request):
    mentee = Mentee.objects.all()
    return render(request, 'Mentee/Mentee.html', {'mentees' : mentee})
