# from django.db import models
# from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.contrib import admin
# from django.db.models.signals import post_save
# from django.dispatch import receiver


# class Keys(models.Model):
    
#     pass

# If new user model instance is created => create coins model instatce
# https://habr.com/ru/post/313764/
    # @receiver(post_save, sender=User)
    # def create_user_coinbox(sender, instance, created, **kwargs):
    #     if created:
    #         Coins.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_coinbox(sender, instance, **kwargs):
    #     instance.coins.save()
    
    # def is_teacher(user):
    #     return user.groups.filter(name='Teacher').exists()