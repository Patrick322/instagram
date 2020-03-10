

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# from django.db

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
    full_name = models.CharField(max_length=255,null=True)
    bio = models.TextField(max_length=50)
    email = models.EmailField(null=True)

def save_user_profile(sender, instance):
    instance.profile.save()

@classmethod
def search_profile(cls,search_teArticlerm):
    profiles = cls.objects.filter(Q(username__username=search_term) | Q(fullname__fullname+search_term)) 
    return profiles

class post(models.Model):
    photo_pic = models.ImageField(upload_to = 'photos/')
    caption = models.CharField(max_length=2000)
    upload_by = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    # post_date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.caption

def save_photo(self, user):
    self.save()

@classmethod
def all_photos(cls):
    all_photos = cls.objects.all()
    return all_photos

@classmethod
def user_photos(user, username):
    photos = cls.objects.filter(upload_by__username=username)
    return photos

@classmethod
def filter_by_caption(cls,search_term):
    return cls.objects.filter(caption__fullname=search_term)

def delete_photos(self, user):
    self.delete()

class Comment(models.Model):
    comment_content = models.CharField(max_length=100)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(post,on_delete=models.CASCADE)

def save_comment(self):
    self.save()

class Like(models.Model):
    models.ForeignKey(User,on_delete=models.CASCADE)
    control = models.CharField(max_length=50,null=True)

def __str__(self):
    return self.control

def save_like(self):
    self.save()

