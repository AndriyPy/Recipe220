from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('AI_assistent.urls')),
    path('google_sso/', include('django_google_sso.urls', namespace="django_google_sso")),

]
