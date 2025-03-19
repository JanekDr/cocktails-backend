from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'cocktails', views.CocktailViewSet, basename='cocktails')
router.register(r'ingredients', views.IngredientViewSet, basename='ingredients')
# router.register(r'cocktail-ingredients', views.CocktailIngredientViewSet, basename='cocktail-ingredients')

urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)