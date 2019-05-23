from rest_framework import serializers
from .models import Recipe, Step, Ingredient


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"