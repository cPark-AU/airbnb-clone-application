from django.db import models

class CommonModel(models.Model):

    """ Common Model Definition """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: # Avoids Django creating a model in the database
        abstract = True