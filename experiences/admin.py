from django.contrib import admin
from .models import Experience, Services

@admin.register(Experience)
class Experience(admin.ModelAdmin):
    pass

@admin.register(Services)
class Services(admin.ModelAdmin):
    pass
