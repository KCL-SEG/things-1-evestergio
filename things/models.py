from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Thing(models.Model):
    name = models.CharField(
        unique=False,
        blank=False,
        max_length=30,
    )
    description = models.CharField(
        unique=True,
        blank=True,
        max_length=120,
    )
    quantity = models.IntegerField(
        unique=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
    )