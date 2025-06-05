
class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama', 'harga', 'deskripsi', 'gambar', 'kategori', 'tersedia', 'spesifikasi']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nama produk'}),
            'harga': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan harga'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Masukkan deskripsi'}),
            'gambar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan path gambar (contoh: produk/images/laptop.jpeg)'}),
            'kategori': forms.Select(attrs={'class': 'form-control'}),
            'tersedia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'spesifikasi': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Masukkan spesifikasi sebagai JSON, contoh: ["Prosesor: Intel Core i7", "RAM: 16GB"]'}),
        }
