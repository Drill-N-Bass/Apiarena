from dataclasses import field
from distutils.command import upload
from django.db import models

# Create your models here.

class EssayCls(models.Model):
    title = models.CharField(max_length=200)
    slug  = models.SlugField(unique=True) 
    description = models.TextField()
    image = models.ImageField(upload_to='images')