from urllib import request
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
        ]

        read_only_fields = ['id']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = [
            'id',
            'name',
            'description',
            'alcoholic',
            'type',
            'percentage',
            'image'
        ]

        read_only_fields = ['id']

    def get_image(self, obj):
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None


class CocktailIngredientSerializer(serializers.ModelSerializer):
    ingredient = serializers.PrimaryKeyRelatedField(queryset=Ingredient.objects.all())

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
            'cocktail_ingredients',
            'alcohol_strength'
        ]
    
    def create(self, validated_data):
        ingredients_data = validated_data.pop('cocktail_ingredients', [])
        cocktail = Cocktail.objects.create(**validated_data)  

        for ingredient_data in ingredients_data:
            ingredient = ingredient_data.pop('ingredient')
            CocktailIngredient.objects.create(cocktail=cocktail, ingredient=ingredient, **ingredient_data)

        return cocktail
    
    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('cocktail_ingredients', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if ingredients_data is not None:
            instance.cocktail_ingredients.all().delete()
            for ingredient_data in ingredients_data:
                ingredient = ingredient_data.pop('ingredient')
                CocktailIngredient.objects.create(
                    cocktail=instance,
                    ingredient=ingredient,
                    **ingredient_data
                )

        return instance