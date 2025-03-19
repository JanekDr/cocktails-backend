from rest_framework import serializers
from .models import Cocktail, Ingredient, CocktailIngredient

class CocktailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktail
        fields = [
            'id',
            'name',
            'category',
            'instruction',
            'glass',
            'alcoholic',
            'created_at',
            'updated_at',
        ]

        read_only_fields = ['id', 'created_at', 'updated_at']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = [
            'id',
            'name',
            'description',
            'alcoholic',
            'type',
            'image'
        ]

        read_only_fields = ['id', 'created_at', 'updated_at']


class CocktailIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = CocktailIngredient
        fields = [
            'id',
            'ingredient',
            'amount',
            'unit'
        ]


class CocktailDetailSerializer(serializers.ModelSerializer):
    cocktail_ingredients = CocktailIngredientSerializer(many=True)

    class Meta:
        model = Cocktail
        fields = [
            'id',
            'name',
            'category',
            'instruction',
            'glass',
            'alcoholic',
            'created_at',
            'updated_at',
            'cocktail_ingredients'
        ]

        read_only_fields = ['id', 'created_at', 'updated_at']