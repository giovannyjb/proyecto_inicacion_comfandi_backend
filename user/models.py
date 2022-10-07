from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class AboutMe(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="about_me")
    img_profile = models.ImageField(upload_to="profiles", null=True)
    cv = models.FileField(upload_to="cv", null=True)
    job_description = models.CharField(max_length=100, default=None, null=True)
    experience = models.CharField(max_length=100)
    clients = models.CharField(max_length=100)
    projects = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=50,default=0)


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='experiences')

    class State(models.IntegerChoices):
        FRONTEND = 0, 'Frontend'
        BACKEND = 1, 'Backend'

    type = models.IntegerField(default=State.FRONTEND, choices=State.choices)
    title = models.CharField(max_length=100)

    class State(models.IntegerChoices):
        LOW = 0, 'LOW'
        MEDIUM = 1, 'MEDIUM'
        HIGH = 2, 'HIGH'

    level = models.IntegerField(default=State.LOW, choices=State.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

