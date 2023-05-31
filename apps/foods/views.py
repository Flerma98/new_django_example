from rest_framework import viewsets

from apps.foods.models import Food
from apps.foods.serializers import FoodSerializer


# Create your views here.
class FoodViewSet(viewsets.ModelViewSet):
    model = Food
    serializer_class = FoodSerializer
    queryset = Food.objects.all()
