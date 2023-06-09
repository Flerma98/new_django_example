from django.db import models

from apps.users.models import User


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    lat = models.FloatField()
    lng = models.FloatField()
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
