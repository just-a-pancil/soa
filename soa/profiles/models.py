from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    image = models.ImageField(default='default.svg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def __getFullName__(self):
        if self.user.last_name and self.user.first_name:
            return f'{self.user.last_name}, {self.user.first_name}'.upper()
        return None
    __getFullName__.short_description = "Фамилия, Имя"

    def __getUsername__(self):
        return f'{self.user.username}'
    __getUsername__.short_description = "Имя Пользователя"

    def __getGroups__(self):
        return ', '.join(self.user.groups.values_list('name',flat=True))
        return None
    __getGroups__.short_description = "Группы"

    def __isActive__(self):
        return '' if self.user.is_active else False
        # return f'{self.user.is_active}'.upper()
        return None
    __isActive__.short_description = "Активирован"

    def __isTeacher__(self):
        return True if "Teacher" in self.user.groups.values_list('name', flat=True) else ''
    __isTeacher__.short_description = "Учитель"
        

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        
    def is_teacher(user):
        return user.groups.filter(name='Teacher').exists()
        