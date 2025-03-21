from django.http import HttpResponse
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Cocktail, Ingredient
from .serializers import (
    CocktailSerializer,
    IngredientSerializer,
    CocktailDetailSerializer
)


# Create your views here.
def index(request):
    return HttpResponse('Hello, world!')


class CocktailViewSet(viewsets.ModelViewSet):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'category', 'glass']
    ordering_fields = ['name', 'category', 'glass','ceated_at', 'updated_at', 'alcohol_strength']
    filterset_fields = ['alcoholic', 'category', 'glass']

    def get_serializer_class(self):
        if self.action in ['retrieve', 'create', 'update', 'partial_update']:
            return CocktailDetailSerializer
        return CocktailSerializer

    @action(detail=False, methods=['get'])
    def filter_by_ingredient(self, request):
        ingredient_name = request.GET.get('ingredient_name')

        if ingredient_name is None:
            return Response({'error': 'ingredient_name is missing'}, status=400)

        try:
            cocktails = Cocktail.objects.filter(cocktail_ingredients__ingredient__name__iexact=ingredient_name)
            serializer = CocktailDetailSerializer(cocktails, many=True).data
            return Response(serializer)
        except:
            return Response({'error': 'cocktails not found'}, status=404)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()) 
        ordering = request.query_params.get('ordering')

        if ordering in ['alcohol_strength', '-alcohol_strength']:
            queryset = sorted(
                queryset, 
                key=lambda c: c.alcohol_strength, 
                reverse=ordering.startswith('-')
            )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'type', 'description', 'type']
    ordering_fields = ['name', 'type','percentage', 'ceated_at', 'updated_at']
    filterset_fields = ['type', 'alcoholic']