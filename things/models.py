from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Thing(models.Model):
    name = models.CharField(
        unique=True,
        blank=False,
        max_length=30,
        null=False,
    )
    description = models.CharField(
        unique=False,
        blank=True,
        max_length=120,
        null=False,
    )
    quantity = models.IntegerField(
        unique=False,
        null=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
    )