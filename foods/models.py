from django.db import models

from restaurants.models import Restaurant


# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.FloatField(max_length=250)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.restaurant.name})'
