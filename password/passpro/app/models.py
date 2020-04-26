from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.PROTECT)
    # this is a model clas with additional information, thats y we didnt inherit User class, because default user doesn't have that,
    # if we want to add extra attribute then have to use OneToOneField

    # additional

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank=True)

    def __str__(self):
        return self.user.username
