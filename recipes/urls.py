from rest_framework import routers
from .views import RecipeViewSet, StepViewSet, IngredientViewSet

router = routers.DefaultRouter()

router.register('api/recipes', RecipeViewSet, 'recipes')
router.register('api/step/', StepViewSet, 'steps')
router.register('api/ingredients', IngredientViewSet, 'ingredients')

urlpatterns = router.urls
