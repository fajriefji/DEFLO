from django.db import models
from django.utils import timezone
from datetime import datetime
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import TextField
from django.db.models import FileField

class Blog(models.Model):
    Foto = models.CharField (max_length=100)
    Posted_at = models.DateTimeField (default=timezone.now)
    Judul = models.CharField(max_length=100)
    Isi = models.TextField(max_length=1000) 

    def __str__ (self):
        return self.Judul