from django.db import models
from django.utils.translation import gettext_lazy as _


class UserType(models.IntegerChoices):
    ADMIN = 0, _('Admin')
    SUPERVISOR = 1, _('Supervisor')
    RESTAURANT = 2, _('Restaurant')
    WORKER = 3, _('Worker')
    CLIENT = 4, _('Client')
