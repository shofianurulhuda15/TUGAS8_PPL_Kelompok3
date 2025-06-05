from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=100)

    def _str_(self):
        return self.nama

class Produk(models.Model):
    nama = models.CharField(max_length=200)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    deskripsi = models.TextField()
    gambar = models.CharField(max_length=200, blank=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    tersedia = models.BooleanField(default=True)
    spesifikasi = models.JSONField(default=list)

    def _str_(self):
        return self.nama
