from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True) 
