from django.db import models

# Create your models here.
class Cocktail(models.Model):
    category_choices = [
        ('soft drink', 'Soft Drink'),
        ('sweet', 'Sweet'),
        ('sour', 'Sour'),
        ('sweet and sour', 'Sweet and Sour'),
        ('dry', 'Dry'), 
        ('bitter', 'Bitter'),
        ('strong', 'Strong'),
        ('sparkling', 'Sparkling'),
        ('creamy', 'Creamy'),
        ('fruity', 'Fruity'),
        ('spicy', 'Spicy'),
        ('hot', 'Hot'),
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
    alcoholic = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def alcohol_strength(self):
        if not self.alcoholic:
            return 0.0
        
        total = 0
        for ci in self.cocktail_ingredients.select_related('ingredient').all():
            if ci.ingredient.alcoholic and ci.ingredient.percentage is not None:
                try:
                    amount = float(ci.amount)
                except ValueError:
                    amount = 0.0

                total += amount * (ci.ingredient.percentage / 100)

        return round(total, 2)  

    def __str__(self):
        return self.name

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
        ('coffee', 'Coffee'),
        ('milk', 'Milk'),
        ('cream', 'Cream'),
        ('egg', 'Egg'),
        ('fruit', 'Fruit'),
        ('herb', 'Herb'),
        ('spice', 'Spice'),
        ('other', 'Other')
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    alcoholic = models.BooleanField(default=True)
    type = models.CharField(max_length=50, choices=type_choices, default='other')
    percentage = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CocktailIngredient(models.Model):
    unit_choices = [
        ('ml', 'ml'),
        ('cl', 'cl'),
        ('g', 'g'),
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
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE, related_name='cocktail_ingredients', null=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.CharField(max_length=50)
    unit = models.CharField(max_length=50, choices=unit_choices, default='ml')

    def __str__(self):
        return f'{self.ingredient.name} - {self.amount} {self.unit}'