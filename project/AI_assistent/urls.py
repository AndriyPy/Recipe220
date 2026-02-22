from django.urls import path
from . import views

urlpatterns = [
    path("ai-test/", views.recipe_ai_view, name="ai_home"),
    path("history/", views.generated_recipe_view, name="ai_history"),
    path("delete/<int:id>", views.delete_recipe_view, name="ai_delete")
]
