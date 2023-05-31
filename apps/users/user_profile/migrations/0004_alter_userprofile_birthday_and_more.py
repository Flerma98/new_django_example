# Generated by Django 4.2.1 on 2023-05-31 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_userprofile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(verbose_name='birthday'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(max_length=250, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='genre',
            field=models.SmallIntegerField(choices=[(0, 'Other'), (1, 'Male'), (2, 'Female')], verbose_name='genre'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(max_length=250, verbose_name='last_name'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=20, unique=True, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='profile_images/', verbose_name='profile_image'),
        ),
    ]