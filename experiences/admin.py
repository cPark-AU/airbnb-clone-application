from django.contrib import admin
from .models import Experience, Services

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "name", 
        "price", 
        "start_time", 
        "end_time", 
        "created_at",
    )

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "details",
        "description",
    )
