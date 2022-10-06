from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class AboutMe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    experience = models.CharField(max_length=100)
    clients = models.CharField(max_length=100)
    projects = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Experience(models.Model):
    class State(models.IntegerChoices):
        FRONTEND = 0, 'Frontend'
        BACKEND = 1, 'Backend'

    type = models.IntegerField(default=State.FRONTEND, choices=State.choices)
    title = models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
