from django.contrib import admin
from .models import Profile
from recipe.models import Recipes


admin.site.register(Recipes)
admin.site.register(Profile)
