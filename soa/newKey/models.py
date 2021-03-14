from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
from secrets import token_urlsafe
import datetime
import datetime as dt
# django alwalys use utc-00 timezone (London), so we comare all to London
from django.utils import timezone
import qrcode
import os


class Keys(models.Model):
    token = models.CharField(max_length=44)
    created = models.DateTimeField(auto_now_add=True)
    createdBy = models.CharField(default='',max_length = 50)
    life = models.DurationField(default=datetime.timedelta(hours=1))   # lifetime of tokens
    amount = models.IntegerField(default=0)  # amount of supported operations
    scanned = models.IntegerField(default=0)
    maxScanned = models.IntegerField(null=True)
    qr = models.ImageField(default='Epilog-Pancake-QR.jpg', upload_to='qrs')

    @classmethod
    def create(cls, request, amount, life):
        key = cls()
        key.__generate_token__()
        key.__generate_qr__()
        key.__generate_group__()
        if amount: key.__set_amount__(amount)
        if life: key.__set_life__(life)
        key.save()
        return key

    def __generate_token__(self):
        self.token = token_urlsafe()

    def __generate_qr__(self):
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,)
        qr.add_data("http://127.0.0.1:8000/transaction/remote/"+self.token)
        qr.make()
        img=qr.make_image()
        img.save("./media/qrs/"+self.token+".png")
        # set qr
        self.qr = self.token+".png"

    def __set_amount__(self, amount):
        self.amount=int(amount)
        
    def __set_life__(self, lifeMinutes):
        self.life = datetime.timedelta(minutes=int(lifeMinutes))

    def __extend_life__(self, extendMinutes=60):
        self.life = self.life+datetime.timedelta(minutes=int(extendMinutes))

    def __str__(self):
        return f'{self.token}'

    def __generate_group__(self):
        Group.objects.get_or_create(name='key_'+self.token)

    def is_valid_by_date(self):
        # now is now() in London
        now = timezone.now()
        deadline = (self.created+self.life)
        return deadline.isoformat() > now.isoformat()

    def is_valid_by_scan_amount(self):
        if not self.maxScanned:
            return True
        if self.scanned < self.maxScanned:
            return True

    def is_valid(self):
        if self.is_valid_by_date() and self.is_valid_by_scan_amount():
            return True
        return False

    def just_scanned(self, *args):
        self.scanned += 1
        self.save()

    def __clear_self__(self):
        Group.objects.filter(name='key_'+self.token).delete()

        import platform, os
        from pathlib import PureWindowsPath, Path, PurePath

        token = self.token
        path = Path(__file__).resolve()
        qrs_path = Path(path.cwd(),'media','qrs')
        code_path = Path(qrs_path, token).with_suffix('.png')
        if code_path.exists():
            if platform.system() == "Windows":
                code_path = PureWindowsPath(code_path)
            else:
                code_path = PurePath(code_path)
                
            os.remove(code_path)

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