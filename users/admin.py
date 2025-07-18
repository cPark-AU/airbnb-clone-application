from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ("Profile", {
            "fields": ("profile_photo","username", "password", "email", "name", "is_host", "gender", "language", "currency"),
            "classes": ("wide",),
        }),
        ("Permissions", {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions"),
            "classes": ("collapse",),
        }),
        ("Important dates", {
            "fields": ("last_login", "date_joined"),
            "classes": ("collapse",),
        }),
    )







