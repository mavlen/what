from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Name(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    
