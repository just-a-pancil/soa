# Generated by Django 3.1.1 on 2020-09-27 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ФИ', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=45)),
                ('Класс', models.CharField(blank=True, max_length=3)),
            ],
        ),
    ]
