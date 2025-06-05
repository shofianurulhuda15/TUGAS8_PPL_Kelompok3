from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Produk, Kategori
from .forms import ProdukForm

def home(request):
    produk_terbaru = Produk.objects.filter(tersedia=True)[:3]
    kategori_list = Kategori.objects.all()
    context = {
        'produk_terbaru': produk_terbaru,
        'kategori_list': kategori_list,
        'judul_halaman': 'Beranda'
    }
    return render(request, 'produk/home.html', context)

def daftar_produk(request):
    kategori_id = request.GET.get('kategori')
    sort = request.GET.get('sort', 'nama_asc')  # Default sort: nama ascending
    
    # Ambil produk berdasarkan kategori
    if kategori_id:
        produk_list = Produk.objects.filter(kategori_id=kategori_id, tersedia=True)
        judul = "Produk dalam kategori tertentu"
    else:
        produk_list = Produk.objects.filter(tersedia=True)
        judul = "Semua Produk"
    
    # Sorting
    if sort == 'nama_asc':
        produk_list = produk_list.order_by('nama')
    elif sort == 'nama_desc':
        produk_list = produk_list.order_by('-nama')
    elif sort == 'harga_asc':
        produk_list = produk_list.order_by('harga')
    elif sort == 'harga_desc':
        produk_list = produk_list.order_by('-harga')
    
    # Paginasi
    paginator = Paginator(produk_list, 6)  # 6 produk per halaman
    page_number = request.GET.get('page')
    produk_list = paginator.get_page(page_number)
    
    kategori_list = Kategori.objects.all()
    context = {
        'produk_list': produk_list,
        'kategori_list': kategori_list,
        'judul_halaman': judul
    }
    return render(request, 'produk/daftar_produk.html', context)

def detail_produk(request, id):
    produk = get_object_or_404(Produk, id=id)
    produk_terkait = Produk.objects.filter(kategori=produk.kategori, tersedia=True).exclude(id=id)[:2]
    context = {
        'produk': produk,
        'produk_terkait': produk_terkait,
        'judul_halaman': produk.nama
    }
    return render(request, 'produk/detail_produk.html', context)

def kontak(request):
    pesan_sukses = None
    if request.method == 'POST':
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        subjek = request.POST.get('subjek')
        pesan = request.POST.get('pesan')
        if nama and email and subjek and pesan:
            messages.success(request, 'Pesan Anda telah berhasil dikirim. Kami akan segera menghubungi Anda.')
        else:
            messages.error(request, 'Semua field wajib diisi!')
    context = {
        'judul_halaman': 'Kontak Kami',
        'pesan_sukses': pesan_sukses
    }
    return render(request, 'produk/kontak.html', context)

def cari_produk(request):
    query = request.GET.get('q', '')
    produk_list = Produk.objects.filter(nama__icontains=query, tersedia=True) if query else []
    context = {
        'produk_list': produk_list,
        'query': query,
        'judul_halaman': f'Hasil Pencarian: {query}' if query else 'Pencarian Produk'
    }
    return render(request, 'produk/daftar_produk.html', context)

def tambah_produk(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produk berhasil ditambahkan!')
            return redirect('daftar_produk')
        else:
            messages.error(request, 'Terdapat kesalahan dalam formulir. Silakan periksa kembali.')
    else:
        form = ProdukForm()
    context = {
        'form': form,
        'judul_halaman': 'Tambah Produk'
    }
    return render(request, 'produk/form_produk.html', context)

def edit_produk(request, id):
    produk = get_object_or_404(Produk, id=id)
    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produk berhasil diperbarui!')
            return redirect('daftar_produk')
        else:
            messages.error(request, 'Terdapat kesalahan dalam formulir. Silakan periksa kembali.')
    else:
        form = ProdukForm(instance=produk)
    context = {
        'form': form,
        'judul_halaman': f'Edit Produk: {produk.nama}'
    }
    return render(request, 'produk/form_produk.html', context)

def hapus_produk(request, id):
    produk = get_object_or_404(Produk, id=id)
    if request.method == 'POST':
        produk.delete()
        messages.success(request, 'Produk berhasil dihapus!')
        return redirect('daftar_produk')
    context = {
        'produk': produk,
        'judul_halaman': f'Hapus Produk: {produk.nama}'
    }
    return render(request, 'produk/hapus_produk.html', context)
