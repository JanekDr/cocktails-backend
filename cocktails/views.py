from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Cocktail, Ingredient
from .serializers import (
    CocktailSerializer,
    IngredientSerializer,
    CocktailIngredientSerializer,
    CocktailDetailSerializer
)


# Create your views here.
def index(request):
    return HttpResponse('Hello, world!')


class CocktailViewSet(viewsets.ModelViewSet):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

    filter_backends = [filters.SearchFilter]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CocktailDetailSerializer
        return CocktailSerializer



class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    filter_backends = [filters.SearchFilter]
