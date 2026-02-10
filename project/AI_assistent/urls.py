from django.urls import path
from . import views

urlpatterns = [
    path("ai-test/", views.recipe_ai_view, name="ai_view"),
]
