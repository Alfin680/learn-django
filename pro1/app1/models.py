from django.contrib.auth.models import User
from django.db import models


class UserDetails(models.Model):
    username = models.CharField(max_length=20,)
    password = models.CharField(max_length=10)

class Blog(models.Model):
    title = models.CharField(max_length= 20)
    content = models.CharField(max_length= 500)

# Create your models here.
