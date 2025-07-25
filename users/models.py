from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")
        OTHER = ("other", "Other")
    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")
        CN = ("cn", "Chinese")
    class CurrencyChoices(models.TextChoices):
        KRW = ("krw", "Korean Won")
        USD = ("usd", "United States Dollar")
        AUD = ("aud", "Australian Dollar")

    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150, default=first_name)
    is_host = models.BooleanField(default=False)
    profile_photo = models.ImageField(blank=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)
    language = models.CharField(max_length=2, choices=LanguageChoices.choices)
    currency = models.CharField(max_length=5, choices=CurrencyChoices.choices)