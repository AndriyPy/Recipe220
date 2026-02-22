from django.contrib import admin
from .models import Profile, EmailVerification
from AI_assistent.models import Recipes


admin.site.register(Profile)
admin.site.register(EmailVerification)
admin.site.register(Recipes)
