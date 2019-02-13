from django.db import models
from django.utils import timezone
from datetime import datetime
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import FileField

class Mentee(models.Model):
    Foto = models.CharField (max_length=100)
    Nama = models.CharField (max_length=100)
    Slogan = models.TextField(max_length=100) 

    def __str__ (self):
        return self.Nama