from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, UserLoginForm
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required



def register_view(request: HttpRequest):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


def login_view(request: HttpRequest):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return redirect('/')
    else:
        form = UserLoginForm()

    return render(request, 'users/login.html', {'form': form})



def logout_view(request: HttpRequest):
    logout(request)
    return redirect('login')

def main_page_view(request: HttpRequest):
    return render(request, "users/main.html")

@login_required
def profile_view(request: HttpRequest):
    return render(request, "users/profile.html")



