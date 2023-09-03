from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name=models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    bio= models.CharField(max_length=100,null=True, blank=True)
    image=models.ImageField(upload_to='uploads/user')
    consistency_score = models.IntegerField(default=50)