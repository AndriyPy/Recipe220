from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name="registration"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("", views.main_page_view, name="main"),
    path("profile/", views.profile_view, name="profile"),

]
