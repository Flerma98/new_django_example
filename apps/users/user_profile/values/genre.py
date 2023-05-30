from django.db import models
from django.utils.translation import gettext_lazy as _


class Genre(models.IntegerChoices):
    OTHER = 0, _('Other')
    MALE = 1, _('Male')
    FEMALE = 2, _('Female')
