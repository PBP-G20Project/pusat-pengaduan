from django.db import models
from login_things.models import User
# Create your models here.

class Draft(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
