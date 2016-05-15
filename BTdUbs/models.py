from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import PhoneNumberField

# Create your models here.
class UserProfile(models.Model):
    #link UserProfile to a User model instance
    user = models.OneToOneField(User)

    #additional attributes we want for our users
    phone = PhoneNumberField()
    text_ok = models.BooleanField()

def __unicode__(self):
    return self.user.username

class Store(models.Model):
    store_name = models.CharField(max_length=1024, unique=True)
    url = models.URLField(max_length=1024)
    
