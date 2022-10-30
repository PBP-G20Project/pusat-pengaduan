from django.db import models

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
    user = models.CharField(max_length=100) # pake object user
    admin = models.CharField(max_length=100) # pake object admin

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