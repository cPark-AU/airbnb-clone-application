from django.db import models
from common.models import CommonModel

class Experience(CommonModel):

    """Experience Model Definition"""

    name = models.CharField(max_length=250)
    country = models.CharField(max_length=50, default="Australia")
    city = models.CharField(max_length=80, default="Melbourne")
    host = models.ForeignKey("users.User", on_delete=models.CASCADE,)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField()
    services = models.ManyToManyField(
        "experiences.Services",
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

class Services(CommonModel):

    """"Service Model Definition : What is included in experience"""

    name = models.CharField(max_length=150)
    details = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name



