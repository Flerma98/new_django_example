from rest_framework import serializers

from apps.restaurants.models import Restaurant
from apps.restaurants.serializers import RestaurantSerializer
from .models import Food
from django.utils.translation import gettext_lazy as _


class FoodSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()

    class Meta:
        model = Food
        fields = '__all__'


class FoodCreationSerializer(serializers.ModelSerializer):
    restaurant_id = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all(),
                                                       required=True,
                                                       write_only=True,
                                                       error_messages={
                                                           'does_not_exist': _('Restaurant not found')
                                                       })

    class Meta:
        model = Food
        fields = ['name', 'calories', 'restaurant_id']

    def create(self, validated_data):
        restaurant = validated_data.pop('restaurant_id')
        food = Food.objects.create(**validated_data, restaurant_id=restaurant.id)
        return food


class FoodEditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'calories']