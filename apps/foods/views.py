from rest_framework import viewsets
from drf_query_filter import fields
from rest_framework.filters import OrderingFilter

from apps.foods.models import Food
from apps.foods.serializers import FoodSerializer


# Create your views here.
class FoodViewSet(viewsets.ModelViewSet):
    model = Food
    serializer_class = FoodSerializer
    queryset = Food.objects.all()

    filter_backends = [OrderingFilter]
    ordering_fields = {
        'id': 'id'
    }

    query_params = [
        fields.Field('name', 'name__icontains'),
        fields.Field('calories', 'calories__icontains'),
        fields.Field('restaurant', 'restaurant.name__icontains')
    ]