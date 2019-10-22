from django.db import models

# Create your models here.
from users.models import UsersProfile


class Feedbacks(models.Model):
    user = models.ForeignKey(UsersProfile, related_name='users', on_delete=models.CASCADE)
    feedback_text = models.TextField(max_length=500)
    ratings = models.IntegerField(max_length=5)
    #created_at = models.DateField(auto_now_add=True)

