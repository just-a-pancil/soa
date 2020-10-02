from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imege = models.ImageField(default='default.jpg', upload_to='profil_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
