from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from foods.models import Food
from foods.serializers import FoodSerializer, FoodCreationSerializer
from django.utils.translation import gettext as _


# Create your views here.
class FoodList(APIView):

    def get(self, request):
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FoodCreationSerializer(data=request.data)
        if serializer.is_valid():
            food = serializer.save()
            food_serializer = FoodSerializer(food)
            return Response(food_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FoodDetail(APIView):

    @staticmethod
    def get_food(pk):
        try:
            return Food.objects.get(pk=pk)
        except Food.DoesNotExist:
            raise NotFound(_('Food not found'))

    def get(self, request, pk):
        food = self.get_food(pk)
        serializer = FoodSerializer(food)
        return Response(serializer.data)

    def put(self, request, pk):
        food = self.get_food(pk)
        serializer = FoodSerializer(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        food = self.get_food(pk)
        serializer = FoodSerializer(food, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        food = self.get_food(pk)
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
