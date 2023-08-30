from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

"""Для модели нашего юзера наследуем юзера из коробки жанги"""
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    friends = models.ManyToManyField("self", blank=True)

    def __str__(self):
        if str(self.first_name) == '' or str(self.last_name) == '':
            return str(self.username)
        else:
            return str(self.first_name) + ' ' + str(self.last_name)
