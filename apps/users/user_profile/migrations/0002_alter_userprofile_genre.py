# Generated by Django 4.2.1 on 2023-05-30 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='genre',
            field=models.SmallIntegerField(choices=[(0, 'Other'), (1, 'Male'), (2, 'Female')]),
        ),
    ]