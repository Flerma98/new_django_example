import os

from django.db import models
from django.utils.crypto import get_random_string

from apps.users.user_profile.values.genre import Genre


def get_file_extension(filename):
    file_extension = os.path.splitext(filename)[1]
    return file_extension


def upload_picture_to(self, filename):
    random_string = get_random_string(length=15)
    new_filename = f"profile_{self.id}_{random_string}{get_file_extension(filename)}"
    return f"profile_images/{new_filename}"


class UserProfile(models.Model):
    first_name = models.CharField(max_length=250, null=False, verbose_name='first_name')
    last_name = models.CharField(max_length=250, null=False, verbose_name='last_name')
    phone = models.CharField(max_length=20, null=False, unique=True, verbose_name='phone')
    birthday = models.DateField(null=False, verbose_name='birthday')
    genre = models.SmallIntegerField(choices=Genre.choices, null=False, verbose_name='genre')
    profile_image = models.ImageField(upload_to=upload_picture_to, null=True, verbose_name='profile_image')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
