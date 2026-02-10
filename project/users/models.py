from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class Profile(AbstractUser):
    gender = models.CharField(
        max_length=6,
        choices=[
            ("Male", "Male"),
            ("Female", "Female"),
        ],
        verbose_name="Gender",
        blank=True,
        null=True
    )


    birth_date = models.DateField(blank=True, null=True, verbose_name="Date of birth")

    country = models.CharField(
        max_length=6,
        choices=[
            ("Ukraine", "Ukraine"),
            ("Germany", "Germany"),
            ("Slovakia", "Slovakia"),
            ("Poland", "Poland"),
            ("USA", "USA"),
            ("Italy", "Italy"),
        ],
        verbose_name="Country",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username


class EmailVerification(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='verifications')
    code = models.CharField(max_length=6)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    def is_expired(self):
        return timezone.now() > self.expires_at

    def __str__(self):
        return f"Email verification for {self.user}"

    def is_valid(self):
        return (
            not self.is_used and
            timezone.now() <= self.expires_at
        )
