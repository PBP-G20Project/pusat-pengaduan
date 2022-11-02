from django.db import models
from django.conf import settings

# Create your models here.

# Report: Judul, Isi Laporan, Tanggal, Lokasi, Instansi, Pihak yang terlibat, Status

class Feedback(models.Model):    
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        null = True,
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.BooleanField(default = True)