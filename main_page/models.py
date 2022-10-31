from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from login_things.models import User


def validate_value(value):
    if value < 0 or value > 5:
        raise ValidationError('Rating Has to Be Between 1 to 5')


class Reviews(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    RATING_CHOICES = (
        (5, "Very Good"),
        (4, "Good"),
        (3, "Mediocre"),
        (2, "Bad"),
        (1, "Very Bad")
    )
    rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    comment = models.TextField(max_length=200)
