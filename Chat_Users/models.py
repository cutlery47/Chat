from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

"""Для модели нашего юзера наследуем юзера из коробки жанги"""
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    friends = models.ManyToManyField("self", blank=True)
    chats = models.ManyToManyField("Chat_Messages.Chat", blank=True)

    def __str__(self):
        if str(self.first_name) == '' or str(self.last_name) == '':
            return str(self.username)
        return str(self.first_name) + ' ' + str(self.last_name)

    class Meta:
        db_table = "Users"

class UserPost(models.Model):
    content = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.content

    class Meta:
        db_table = "UserPosts"


