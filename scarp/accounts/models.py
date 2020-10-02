from django.db import models

class Person(models.Model):
    ФИ = models.CharField(max_length=30)
    email = models.EmailField(max_length=45, blank=True)
    Класс = models.CharField(max_length=3, blank=True)
    Пароль = models.CharField(max_length=30, blank=True)
    