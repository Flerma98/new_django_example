# Generated by Django 4.2.1 on 2023-06-09 16:53

import apps.users.user_profile.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=250, verbose_name='last_name')),
                ('phone', models.CharField(max_length=20, unique=True, verbose_name='phone')),
                ('birthday', models.DateField(verbose_name='birthday')),
                ('genre', models.SmallIntegerField(choices=[(0, 'Other'), (1, 'Male'), (2, 'Female')], verbose_name='genre')),
                ('profile_image', models.ImageField(null=True, upload_to=apps.users.user_profile.models.upload_picture_to, verbose_name='profile_image')),
            ],
        ),
    ]
