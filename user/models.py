from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class User(models.Model):
        name = models.CharField(max_length = 100)
        email = models.CharField(max_length = 200)
        password = models.CharField(max_length= 200)
        status = models.IntegerField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

