# Generated by Django 3.1.2 on 2021-02-14 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newKey', '0006_auto_20210214_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keys',
            name='key',
        ),
        migrations.AddField(
            model_name='keys',
            name='token',
            field=models.CharField(default='5DBmva-WTGCGgdvOs9hooqD5Rcs1zyFYriR3a00eK6M', max_length=44),
        ),
    ]
