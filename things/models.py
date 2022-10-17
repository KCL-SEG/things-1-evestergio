from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class Thing(AbstractUser):
    name = models.TextField(
        unique = True,
        blank = False,
        max_length = 30,
    )
    description = models.TextField(
        unique = False,
        blank = True,
        max_length = 120,
    )
    quantity = models.IntegerField(
        unique = False,
        #blank = False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )