from django.db import models
from django.contrib.auth import get_user_model  # gets current user

# Create your models here.


class Recipe(models.Model):
  # one recipe to one user
  owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
  name = models.CharField(max_length=200, null=False, blank=True, unique=True)
  # one to many steps
  # one to many ingredients
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.name

  class Meta:
      verbose_name_plural = "Recipes"


class Step(models.Model):
  step_text = models.CharField(max_length=200, null=False, blank=True)
  # many to one recipe
  recipe = models.ForeignKey(Recipe, related_name='steps', on_delete=models.CASCADE)

  def __str__(self):
      return self.step_text

  class Meta:
      verbose_name_plural = "Steps"
      unique_together = ('recipe', 'step_text')


class Ingredient(models.Model):
  text = models.CharField(max_length=200, null=False, blank=True)
  # many to one recipe
  recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)

  def __str__(self):
      return self.text

  class Meta:
      verbose_name_plural = "Ingredients"
      unique_together = ('recipe', 'text')
