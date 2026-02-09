from django.contrib.auth.models import AbstractUser
from django.db import models

class Profile(AbstractUser):
    gender = models.CharField(
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