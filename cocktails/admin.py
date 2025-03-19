from django.contrib import admin
from .models import Cocktail, CocktailIngredient, Ingredient

# Register your models here.
admin.site.register(Cocktail)
admin.site.register(CocktailIngredient)
admin.site.register(Ingredient)