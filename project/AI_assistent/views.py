from django.shortcuts import render, redirect
from openrouter import OpenRouter
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Recipes


def recipe_ai_view(request):
    recipe = None
    ingredients = request.GET.get("ingredients")

    if ingredients:
        with OpenRouter(api_key=settings.OPEN_ROUTER) as client:
            response = client.chat.send(
                model="mistralai/mistral-7b-instruct",
                messages=[
                    {"role": "user",
                     "content": f"""You are a professional recipe generator. Create a detailed recipe based on this request: "{ingredients}"

FIRST, ANALYZE THE INPUT:
- If the input contains ANY food-related words (like: make, cook, bake, prepare, recipe for, cake, eggs, butter, milk, flour, sugar, etc.), you MUST generate a recipe
- Only reject if the input contains ZERO food items and is clearly non-food (furniture, electronics, office supplies, etc.)
- Commands like "make a cake", "cook dinner", "bake cookies" ARE valid requests
- Lists of ingredients like "eggs, butter, milk" ARE valid requests
- Questions like "how to make pancakes" ARE valid requests
- If in doubt, GENERATE A RECIPE (better to create something than to reject)

STRICT FORMATTING RULES:
1. First line MUST be ONLY the recipe name (no numbers, no "Recipe:" prefix, no quotes)
2. Then ONE empty line
3. Then "Ingredients:" on its own line
4. Group ingredients by categories if needed (e.g., "For the cake:", "For the frosting:") with each category on its own line followed by ingredients indented with "- "
5. Each ingredient MUST include specific quantities (cups, grams, tablespoons, etc.) - use standard measurements
6. Then ONE empty line after all ingredients
7. Then "Instructions:" on its own line
8. Then numbered steps (1., 2., 3. etc.) with each step on a new line
9. Instructions must be detailed, step-by-step, and easy for beginners to follow
10. NO blank lines inside ingredients list or instructions list
11. NO markdown symbols (*, #, -, ---) except the "- " for ingredients
12. NO emojis
13. NO additional text before or after the recipe
14. NO explanations, NO tips, NO notes
15. Recipe must be realistic and achievable with normal cooking techniques
16. Use the provided ingredients as a base, but you CAN add additional common ingredients to make the recipe complete and delicious (salt, pepper, oil, baking powder, vanilla, etc.)

EXAMPLE OF EXACT CORRECT FORMAT:
Classic Butter Cake

Ingredients:
- 2 cups all-purpose flour
- 1 cup granulated sugar
- ½ cup unsalted butter, softened
- 2 large eggs
- ¾ cup milk
- 2 teaspoons baking powder
- 1 teaspoon vanilla extract
- ¼ teaspoon salt

Instructions:
1. Preheat oven to 350°F. Grease a 9-inch cake pan.
2. In a large bowl, cream butter and sugar until light and fluffy.
3. Beat in eggs one at a time, then stir in vanilla.
4. In a separate bowl, whisk flour, baking powder, and salt.
5. Gradually add dry ingredients to wet mixture, alternating with milk.
6. Pour batter into prepared pan and bake for 30-35 minutes.
7. Let cool in pan for 10 minutes, then transfer to wire rack.

If the input contains ABSOLUTELY NO food-related words (zero cooking terms, zero ingredients, only non-food items like "chair table lamp"), respond with ONE short humorous sentence ONLY. Examples:
- "My kitchen runs on food, not furniture. Try again with actual ingredients!"
- "I can't turn a chair into a cake. Need real food items here."
- "Even my smart algorithms can't cook with office supplies. Got any food?"
- "That's an interesting... snack? I'll wait for real ingredients."

INPUT TO PROCESS: {ingredients}"""}
                ],
                max_tokens=600
            )
            recipe = response.choices[0].message.content

            if request.user.is_authenticated:
                Recipes.objects.create(
                    user=request.user,
                    ingredients=ingredients,
                    recipe=recipe
                )

    return render(request, "ai/recipe_ai.html", {"recipe": recipe})



@login_required()
def generated_recipe_view(request):
    recipes = request.user.recipes.all().order_by("-created_at")
    return render(request, "ai/my_recipes.html", {"recipes": recipes})

@login_required
def delete_recipe_view(request, id):
    recipe = Recipes.objects.get(id=id, user=request.user)
    recipe.delete()
    return redirect("my_recipes")