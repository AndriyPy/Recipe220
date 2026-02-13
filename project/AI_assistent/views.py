
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


