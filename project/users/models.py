from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Profile(AbstractUser):
    gender = models.CharField(
        max_length=8,
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
        max_length=8,
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
        

class Recipe(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=200, db_column='Name')
    image_url = models.CharField(max_length=500, db_column='Image URL', blank=True, null=True)
    rating = models.CharField(max_length=50, db_column='Rating', blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    prep_time = models.CharField(max_length=50, db_column='Prep Time', blank=True, null=True)
    cook_time = models.CharField(max_length=50, db_column='Cook Time', blank=True, null=True)
    total_time = models.CharField(max_length=50, db_column='Total Time', blank=True, null=True)
    servings = models.CharField(max_length=50, db_column='Servings', blank=True, null=True)
    ingredients = models.TextField(db_column='Ingredients', blank=True, null=True)

    class Meta:
        db_table = 'recipes'
        managed = False
        
    def __str__(self):
        return f"{self.id} - {self.name}"

