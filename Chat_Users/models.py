from django.db import models
# Create your models here.

"""Модели - объекты с помощью которых можно программно взаимодействовать с базой данных
С помощью модели юзера мы можем добавлять данные о юзерах в таблицу юзеров в бд"""

class User(models.Model):
    firstname = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    password = models.CharField()
    email = models.EmailField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(User.firstname)