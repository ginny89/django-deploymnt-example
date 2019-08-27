from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#To add additional options to basic User class
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    #install pip install pillow to deal with media files

    def __str__(self):
        return self.user.username
