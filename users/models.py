from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, Group


# Create your models here.
USER_TYPE_CHOICES = (
    ('A', 'Admin'),
    ('C', 'Customers')
)

class UsersProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
    user_name = models.CharField(unique=True, max_length=40)
    email = models.CharField(max_length=60)
    user_type = models.CharField(max_length=5, choices=USER_TYPE_CHOICES)
    modified_date = models.DateField(auto_now_add=True)
