from django.contrib import admin
from .models import Recipes


@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'created_at']
    list_display_links = ['id', 'title']
    list_filter = ['created_at']
    search_fields = ['title', 'ingredients', 'user__username']
    readonly_fields = ['created_at']
    ordering = ['-created_at']4
    list_per_page = 25
