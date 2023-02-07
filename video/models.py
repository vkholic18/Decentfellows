from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)

    address = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=30, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)


# Create your models here.
class Video(models.Model):
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to="video/%y")
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True)
    time = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.caption
    
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()




