from django.db import models

from apps.users.user_profile.values.genre import Genre


# Create your models here.
class UserProfile(models.Model):
    first_name = models.CharField(max_length=250, null=False)
    last_name = models.CharField(max_length=250, null=False)
    phone = models.CharField(max_length=20, null=False, unique=True)
    birthday = models.DateField(null=False)
    genre = models.SmallIntegerField(choices=Genre.choices, null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
