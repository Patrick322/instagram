from django.contrib import admin
from .models import Profile,post,Comment,Location,Like

# Register your models here.
admin.site.register(Profile)
admin.site.register(post)
admin.site.register(Comment)
admin.site.register(Location)
admin.site.register(Like)
