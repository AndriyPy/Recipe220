from django.shortcuts import render
from openrouter import OpenRouter
import os
from recipe.models import Recipes

def recipe_ai_view(request):
    recipe = None
    ingredients = request.GET.get("ingredients")

    if ingredients:
        with OpenRouter(api_key="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") as client:
            response = client.chat.send(
                model="mistralai/mistral-7b-instruct",
                messages=[
                    {"role": "user", "content": f"Create a simple recipe using: {ingredients}"}
                ],
                max_tokens=500
            )
            recipe = response.choices[0].message.content

        if request.user.is_authenticated:
            Recipes.objects.create(
                user = request.user,
                ingredients = ingredients,
                recipe = recipe
            )

    return render(request, "ai/recipe_ai.html", {"recipe": recipe})




