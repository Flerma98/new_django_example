from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.user_profile.models import UserProfile
from apps.users.values.user_type import UserType


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError(_('Username is required'))

        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('user_type', UserType.ADMIN)
        return self.create_user(username, password, **extra_fields)


class User(AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(verbose_name=_('username'),
                                unique=True,
                                null=False,
                                max_length=150,
                                validators=[username_validator])
    user_type = models.SmallIntegerField(choices=UserType.choices, default=UserType.CLIENT, null=False)
    profile = models.OneToOneField(UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    date_time_created = models.DateTimeField(auto_now_add=True, null=False, )

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    def __str__(self):
        return self.username
