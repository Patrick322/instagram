from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db

# Create your models here
class Location(models.Model):
    location_name = models.CharField(max_length=30)

def __str__(self):
    return self.location_name

def save_location(self):
    self(save)