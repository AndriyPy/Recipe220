from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
import random
from datetime import timedelta
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string

from .forms import UserRegisterForm, UserLoginForm, EmailVerificationForm, UserEditProfileForm
from .models import Profile, EmailVerification, Recipe

import requests
from django.conf import settings

from django_ratelimit.decorators import ratelimit




def verify_turnstile(token: str):
    if not token:
        return False

    response = requests.post(
          "https://challenges.cloudflare.com/turnstile/v0/siteverify",
        data={
            "secret": settings.TURNSTILE_SECRET_KEY,
            "response": token
        },
        timeout=5
    )

    result = response.json()
    return result.get("success", False)



@ratelimit(key='ip', rate='3/m', block=True)
def register_view(request: HttpRequest):
    if request.method == "POST":
        token = request.POST.get("cf-turnstile-response")

        if not verify_turnstile(token):
            messages.error(request, "Bot verification failed.")
            form = UserRegisterForm(request.POST)
            return render(request, "users/register.html", {
                "form": form,
                "TURNSTILE_SITE_KEY": settings.TURNSTILE_SITE_KEY
            })

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            code = str(random.randint(100000, 999999))

            verification = EmailVerification.objects.create(
                user=user,
                code=code,
                expires_at=timezone.now() + timedelta(minutes=10)
            )

            email_message = EmailMessage(
                subject='Email confirmation',
                body=render_to_string(
                    'mailing/email_verification.html',
                    context={
                        'code': code,
                        'user': user,
                    }
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[user.email],
            )
            email_message.content_subtype = 'html'
            email_message.send(fail_silently=False)

            request.session['verify_user_id'] = user.id
            return redirect('verify_email')

    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form, "TURNSTILE_SITE_KEY": settings.TURNSTILE_SITE_KEY})


@ratelimit(key='ip', rate='3/m', block=True)
def login_view(request: HttpRequest):
    if request.method == 'POST':

        token = request.POST.get("cf-turnstile-response")
        if not verify_turnstile(token):
            messages.error(request, "Bot verification failed.")
            form = UserLoginForm(request.POST)
            return render(request, "users/login.html", {
                "form": form,
                "TURNSTILE_SITE_KEY": settings.TURNSTILE_SITE_KEY
            })

        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return redirect('/')
    else:
        form = UserLoginForm()

    return render(request, 'users/login.html', {'form': form, 'TURNSTILE_SITE_KEY': settings.TURNSTILE_SITE_KEY})


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserEditProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserEditProfileForm()

    return render(request, "users/edit_profile.html", {"form": form})




def logout_view(request: HttpRequest):
    logout(request)
    return redirect('login')

def main_page_view(request: HttpRequest):
    return render(request, "users/main.html")

@login_required
def profile_view(request: HttpRequest):
    return render(request, "users/profile.html")


def email_verification_view(request: HttpRequest):
    user_id = request.session.get("verify_user_id")
    if not user_id:
        messages.error(request, 'Session expired. Please register again.')
        return redirect("registration")

    verification = EmailVerification.objects.filter(
        user_id=user_id,
        is_used=False
    ).order_by("-created_at").first()

    if not verification:
        messages.error(request, 'Verification code not found or expired.')
        return redirect("registration")

    if request.method == "POST":
        form = EmailVerificationForm(request.POST)
        if form.is_valid():
            if not verification.is_valid():
                messages.error(request, 'Code has expired')
                return redirect("registration")

            if form.cleaned_data["code"] == verification.code:
                user = verification.user
                user.is_active = True
                user.save()

                verification.is_used = True
                verification.save()

                request.session.pop("verify_user_id", None)
                login(request, user)
                messages.success(request, 'Email verification has been successfully completed.')

                return redirect("main")
            else:
                messages.error(request, 'The verification code you entered is invalid.')
    else:
        form = EmailVerificationForm()

    context = {
        "form": form,
        "masked_email": verification.user.email[:3] + "***" + verification.user.email[verification.user.email.find('@'):]
    }

    return render(request, "users/verify_email.html", context)


def about_view(request: HttpRequest):
    return render(request, "users/about.html")


def recipe_list(request):
    recipes_list = Recipe.objects.using('recipes_db').all()
    
    paginator = Paginator(recipes_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'recipes/recipe_list.html', {'page_obj': page_obj})

