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
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserLoginForm, EmailVerificationForm, UserEditProfileForm
from .models import Profile, EmailVerification, Recipe
import requests
from django.conf import settings
from django_ratelimit.decorators import ratelimit
from rapidfuzz import process, fuzz


def verify_turnstile(token: str):
    """Check Cloudflare Turnstile token, return True if valid"""
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
    """Handle user registration with CAPTCHA and email verification"""
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
    """Handle user login with CAPTCHA verification"""
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


def email_verification_view(request: HttpRequest):
    """Verify email code and activate user"""
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
        "masked_email": verification.user.email[:3] + "***" + verification.user.email[
                                                              verification.user.email.find('@'):]
    }

    return render(request, "users/verify_email.html", context)


def logout_view(request: HttpRequest):
    """Log out user"""
    logout(request)
    return redirect('login')


@login_required
def edit_profile(request):
    """Edit user profile info"""
    user = request.user
    if request.method == "POST":
        form = UserEditProfileForm(data=request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get('username')
            user.gender = form.cleaned_data.get('gender')
            user.birth_date = form.cleaned_data.get('birth_date')
            user.country = form.cleaned_data.get('country')
            user.save()
            return redirect("profile")

    else:
        form = UserEditProfileForm(initial={
            'username': user.username,
            'gender': user.gender,
            'birth_date': user.birth_date,
            'country': user.country})

    return render(request, "users/edit_profile.html", {"form": form})


@login_required(login_url=reverse_lazy('login'))
def profile_view(request: HttpRequest):
    """Show user profile page"""
    return render(request, "users/profile.html")


def recipe_list(request):
    """Show paginated recipes with trigram fuzzy search"""
    db_name = 'recipes_db'
    search_query = request.GET.get('search', '').strip()

    if search_query:
        all_recipes = list(Recipe.objects.using(db_name).values_list('id', 'name'))

        matches = process.extract(
            search_query,
            [r[1] for r in all_recipes],
            scorer=fuzz.WRatio,
            limit=50,
            score_cutoff=65
        )

        matched_ids = [all_recipes[m[2]][0] for m in matches]

        preserved_order = {pk: i for i, pk in enumerate(matched_ids)}
        queryset = Recipe.objects.using(db_name).filter(id__in=matched_ids)
        recipes_list = sorted(queryset, key=lambda x: preserved_order.get(x.id))
    else:
        recipes_list = Recipe.objects.using(db_name).all()

    paginator = Paginator(recipes_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'recipes/recipe_list.html', {
        'page_obj': page_obj,
        'search_query': search_query
    })


def about_view(request: HttpRequest):
    """Render About page"""
    return render(request, "users/about.html")


def main_page_view(request: HttpRequest):
    """Render homepage"""
    return render(request, "users/main.html")
