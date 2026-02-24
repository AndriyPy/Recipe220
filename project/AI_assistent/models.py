from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Recipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    title = models.CharField(max_length=100, default="Untitled recipe")
    ingredients = models.TextField()
    recipe = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"
