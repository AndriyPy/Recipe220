from django.urls import path
from . import views

urlpatterns = [
    path("ai-test/", views.recipe_ai_view, name="ai_home"),
    path("history/", views.generated_recipe_view, name="ai_history"),
    path("delete/<int:id>", views.delete_recipe_view, name="ai_delete"),
    path("public_recipes/", views.public_recipes, name="public_recipes"),
    path("make_public/<int:id>", views.make_public, name="make_public"),
    path("detail_recipe/<int:id>", views.detail_recipe, name="recipe_detail")
]
