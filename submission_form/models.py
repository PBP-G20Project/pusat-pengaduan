from django.db import models
from django.conf import settings


# Create your models here.

# Report: Judul, Isi Laporan, Tanggal, Lokasi, Instansi, Pihak yang terlibat, Status

INSTITUTION_LEVEL = (
    ('Nasional', 'Nasional'),
    ('Provinsi', 'Provinsi'),
    ('Kabupaten/Kota', 'Kabupaten/Kota'),
    ('Kecamatan', 'Kecamatan'),
    ('Desa/Kelurahan', 'Desa/Kelurahan'),
)
class Report(models.Model):
    user_submission = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='user_submission'
    )
    
    admin_submission = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='admin_submission'
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    institution = models.CharField(max_length=100)
    institution_level = models.CharField(max_length=100, choices=INSTITUTION_LEVEL)
    involved_party = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    def update_status_diproses(self):
        self.status = 'DIPROSES'
    
    def update_status_selesai(self):
        self.status = 'SELESAI'

    def update_status_ditolak(self):
        self.status = 'DITOLAK'