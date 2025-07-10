from django.db import models

# House Model
class House(models.Model):

    """Model Definition for House"""
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=255)
    pets_allowed = models.BooleanField(default=True)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()

# __str__ method is used to return a string representation of the object
def __str__(self):
    return self.name
    