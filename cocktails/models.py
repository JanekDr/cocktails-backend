from django.db import models

# Create your models here.
class Cocktail(models.Model):
    category_choices = [
        ('soft drink', 'Soft Drink'),
        ('alcoholic', 'Alcoholic'),
        ('non-alcoholic', 'Non-Alcoholic'),
        ('hot drink', 'Hot Drink'),
        ('shot', 'Shot'),
        ('punch', 'Punch'),
        ('cocktail', 'Cocktail'),
        ('beer', 'Beer'),
        ('wine', 'Wine'),
        ('champagne', 'Champagne'),
        ('liqueur', 'Liqueur'),
        ('other', 'Other')
    ]

    glass_choices = [
        ('highball', 'Highball'),
        ('whiskey', 'Whiskey'),
        ('martini', 'Martini'),
        ('margarita', 'Margarita'),
        ('collins', 'Collins'),
        ('pint', 'Pint'),
        ('champagne', 'Champagne'),
        ('shot', 'Shot'),
        ('punch', 'Punch'),
        ('beer', 'Beer'),
        ('wine', 'Wine'),
        ('cocktail', 'Cocktail'),
        ('other', 'Other')
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=category_choices)
    instruction = models.TextField()
    glass = models.CharField(max_length=50, choices=glass_choices)
    alcoholic = models.BooleanField()
    cocktail_ingredients = models.ManyToManyField('CocktailIngredient', related_name='cocktail_ingredients')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CocktailIngredient(models.Model):
    unit_choices = [
        ('ml', 'ml'),
        ('cl', 'cl'),
        ('oz', 'oz'),
        ('tsp', 'tsp'),
        ('tbsp', 'tbsp'),
        ('dash', 'dash'),
        ('piece', 'piece'),
        ('slice', 'slice'),
        ('wedge', 'wedge'),
        ('leaf', 'leaf'),
        ('pinch', 'pinch'),
        ('drop', 'drop'),
        ('cup', 'cup'),
        ('shot', 'shot'),
        ('bottle', 'bottle'),
        ('can', 'can'),
        ('bunch', 'bunch'),
        ('bottle', 'bottle'),
        ('other', 'other')
    ]

    id = models.AutoField(primary_key=True)
    ingredient = models.OneToOneField('Ingredient', on_delete=models.CASCADE)
    amount = models.CharField(max_length=50)
    unit = models.CharField(max_length=50, choices=unit_choices, default='ml')

    def __str__(self):
        return f'{self.ingredient.name} - {self.amount} {self.unit}'


class Ingredient(models.Model):
    type_choices = [
        ('vodka', 'Vodka'),
        ('rum', 'Rum'),
        ('whiskey', 'Whiskey'),
        ('gin', 'Gin'),
        ('tequila', 'Tequila'),
        ('brandy', 'Brandy'),
        ('liqueur', 'Liqueur'),
        ('wine', 'Wine'),
        ('beer', 'Beer'),
        ('champagne', 'Champagne'),
        ('soda', 'Soda'),
        ('juice', 'Juice'),
        ('syrup', 'Syrup'),
        ('cola', 'Cola'),
        ('other', 'Other')
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    alcoholic = models.BooleanField(default=True)
    type = models.CharField(max_length=50, choices=type_choices, default='other')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name