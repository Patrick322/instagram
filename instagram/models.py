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

@classmethod
def delete_location(cls,location):
    cls.object.filter(location).delete()

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='photos/',null=True)
    full_name = models.Charfield(max_length=255,null=True)
    username = models.CharField(user,on delete=model.CASCADE,related_name='profile')
    bio = models.TextField(max_length=50)
    email = models.EmailField(null=True)
    phonenumber = models.IntegerField(null=True)
    gender = models.Charfield(max_length=20,)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()    
