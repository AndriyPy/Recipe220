from django.shortcuts import render
from openrouter import OpenRouter
import os

def recipe_ai_view(request):
    ingredients = request.GET.get("grass, cucumber, carrot, beef, ketchup, potato")

    with OpenRouter("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") as client:
        response = client.chat.send(
            model="minimax/minimax-m2",
            messages=[{"role": "user", "content": f"Create a recipe with: {ingredients}"}],
            max_tokens=4000
        )

        text = response.choices[0].message.content

    return render(request, "ai/recipe_ai.html", {"recipe": text})
