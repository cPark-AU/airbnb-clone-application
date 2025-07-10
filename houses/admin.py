from django.contrib import admin
from .models import House

@admin.register(House) # decorator to register the model with the admin site
class HouseAdmin(admin.ModelAdmin):
    
    list_display = [
        "name",
        "price_per_night",
        "address",
        "pets_allowed"
    ]
    list_filter = ["price_per_night", "pets_allowed"] # adds a filter to the admin site
    search_fields = ["name", "address"] # adds a search bar to the admin site
    ordering = ["price_per_night"] # adds a sorting option to the admin site