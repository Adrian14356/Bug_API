from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.TextField()

    def __str__(self):
        return self.name

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key = True)
    username = models.CharField(max_length = 20)

    def __str__(self):
        return self.username



