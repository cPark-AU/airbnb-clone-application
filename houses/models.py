from django.db import models

# House Model
class House(models.Model):

    """Model Definition for House"""
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(verbose_name="Price", help_text="Price per night in AUD")
    description = models.TextField()
    address = models.CharField(max_length=255)
    pets_allowed = models.BooleanField(verbose_name="Pets Allowed?",default=True, help_text="Is pets allowed?")
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()

# __str__ method is used to return a string representation of the object
def __str__(self):
    return self.name
    