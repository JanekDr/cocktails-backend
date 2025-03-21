# Generated by Django 5.1.7 on 2025-03-20 23:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0009_alter_cocktail_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cocktail',
            name='cocktail_ingredients',
        ),
        migrations.AddField(
            model_name='cocktailingredient',
            name='cocktail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cocktail_ingredients', to='cocktails.cocktail'),
        ),
        migrations.AlterField(
            model_name='cocktailingredient',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cocktails.ingredient'),
        ),
    ]
