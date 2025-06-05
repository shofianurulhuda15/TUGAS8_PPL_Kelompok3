from django.urls import path, include
from django.contrib import admin
from produk import views

urlpatterns = [
    path('', views.home, name='home'),  # Halaman beranda
    path('produk/', views.daftar_produk, name='daftar_produk'),  # Daftar semua produk
    path('produk/<int:id>/', views.detail_produk, name='detail_produk'),  # Detail produk berdasarkan ID
    path('kontak/', views.kontak, name='kontak'),  # Halaman kontak
    path('cari/', views.cari_produk, name='cari_produk'),  # Pencarian produk
    path('produk/tambah/', views.tambah_produk, name='tambah_produk'),  # Tambah produk
    path('produk/edit/<int:id>/', views.edit_produk, name='edit_produk'),  # Edit produk
    path('produk/hapus/<int:id>/', views.hapus_produk, name='hapus_produk'),  # Hapus produk
    path('admin/', admin.site.urls),  # URL untuk Django Admin
]