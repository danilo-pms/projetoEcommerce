from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    def __str__(self):
        return self.username