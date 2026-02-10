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
from django.conf import settings

from .forms import UserRegisterForm, UserLoginForm, EmailVerificationForm
from .models import Profile, EmailVerification

def register_view(request: HttpRequest):
    if request.method == "POST":
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
    return redirect('login') #test

def main_page_view(request: HttpRequest):
    return render(request, "users/main.html")

@login_required
def profile_view(request: HttpRequest):
    return render(request, "users/profile.html")



