from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings


def validate_value(value):
    if value < 0 or value > 5:
        raise ValidationError('Rating Has to Be Between 1 to 5')


class Reviews(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(validators=[validate_value])
    comment = models.TextField(max_length=200)
