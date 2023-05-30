from curses.ascii import isalnum

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from django.db import models

from apps.users.user_profile.models import UserProfile
from apps.users.values.user_type import UserType
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser):
    username = models.CharField(_('username'), unique=True, null=False, max_length=150,
                                validators=[RegexValidator(r'^[\w.@+-]+$',
                                                           _('Username can only contain letters, numbers or an valid email'))])
    user_type = models.SmallIntegerField(choices=UserType.choices, default=UserType.CLIENT, null=False)
    profile = models.OneToOneField(UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    date_time_created = models.DateTimeField(auto_now_add=True, null=False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
