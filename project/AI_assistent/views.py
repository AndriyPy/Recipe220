
from django.shortcuts import render
from openrouter import OpenRouter
import os

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

    return render(request, "ai/recipe_ai.html", {"recipe": recipe})


