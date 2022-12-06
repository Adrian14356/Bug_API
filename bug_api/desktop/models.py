from django.db import models
from django.contrib.auth.models import User
from user.models import Project

class Bug(models.Model):
    id = models.IntegerField(primary_key = True)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.CharField(max_length = 100)

    def __str__(self):
        return self.description
