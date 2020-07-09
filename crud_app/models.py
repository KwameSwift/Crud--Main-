from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models.signals import post_save


class userProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="profile")
    company = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)




