from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField('Correo Electronico', max_length=200, unique=True)
    password = models.CharField(max_length=200)

    class Status(models.IntegerChoices):
        ACTIVE = 1,
        INACTIVE = 0

    status = models.IntegerField(default=Status.ACTIVE, choices=Status.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
