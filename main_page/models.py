from django.db import models
# from .models import User

# Create your models here.
class News(models.Model) :
    order = models.TextField()

class Comments(models.Model) :
    order = models.ForeignKey("News", on_delete=models.CASCADE, null = True)
    comment = models.TextField(max_length=200)