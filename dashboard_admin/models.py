from django.db import models
from django.conf import settings

# Create your models here.

# Report: Judul, Isi Laporan, Tanggal, Lokasi, Instansi, Pihak yang terlibat, Status

ALL_STATUS = (
    ('Positif', 'Positif'),
    ('Negatif', 'Negatif'),
)

class Feedback(models.Model):    
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        null = True,
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.CharField(max_length=100, choices=ALL_STATUS)