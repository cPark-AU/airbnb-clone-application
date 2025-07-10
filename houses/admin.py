from django.contrib import admin
from .models import House

@admin.register(House) # decorator to register the model with the admin site
class HouseAdmin(admin.ModelAdmin):
    pass # inherits everything from the ModelAdmin class
