# Generated by Django 3.1.2 on 2021-02-14 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newKey', '0004_auto_20210214_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keys',
            name='key',
            field=models.CharField(default='qQTYfdHXQNnwfy4hEGHoydPCqfBJvWzXM_3KS-3TYCU', max_length=44),
        ),
    ]