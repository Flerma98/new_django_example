from rest_framework import serializers
from .models import Restaurant
from django.utils.translation import gettext_lazy as _

from ..users.values.user_type import UserType


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
        extra_kwargs = {
            'owner': {'read_only': True}
        }


class RestaurantCreationSerializer(serializers.ModelSerializer):
    owner_id = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all(),
                                                  required=False,
                                                  write_only=True,
                                                  error_messages={
                                                      'does_not_exist': _('Owner not found')
                                                  })

    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'lat', 'lng', 'owner_id']

    def create(self, validated_data):
        request = self.context.get('request')

        if request and request.user.user_type != UserType.RESTAURANT:
            owner = validated_data.pop('owner_id')
            restaurant = Restaurant.objects.create(**validated_data, owner_id=owner.id)
        else:
            restaurant = Restaurant.objects.create(**validated_data, owner_id=request.user.id)
        return restaurant


class RestaurantEditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'lat', 'lng']
