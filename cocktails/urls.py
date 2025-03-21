from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'cocktails', views.CocktailViewSet, basename='cocktails')
router.register(r'ingredients', views.IngredientViewSet, basename='ingredients')
# router.register(r'cocktail-ingredients', views.CocktailIngredientViewSet, basename='cocktail-ingredients')

urlpatterns = [
    path('', include(router.urls)),
]