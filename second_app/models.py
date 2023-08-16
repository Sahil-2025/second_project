from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    # This is a relationship, not an inheritance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add additional attributes
    portfolio_site = models.URLField(blank=True)

    #profile_pic = models.ImageField(upload_to='second_app/profile_pics',blank=True)
    profile_pic = models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.user.username + " - " + self.user.first_name + " " + self.user.last_name