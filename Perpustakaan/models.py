from django.db import models

# Create your models here.

class anggota(models.Model) :
    nim_anggota = models.CharField(max_length=12)
    nama_anggota = models.CharField(max_length=100)
    alamat = models.TextField()

    def __str__(self) -> str:
        return f"{self.nim_anggota}"

class buku(models.Model) :
    judul_buku = models.CharField(max_length=100)
    kategori_buku = models.TextField()

    def __str__(self) -> str:
        return f"{self.judul_buku}"

class daftar_hadir(models.Model) :
    nama_anggota = models.CharField(max_length=100)
    tgl_kunjungan = models.DateField(blank=True)

    def __str__(self) -> str:
        return f"{self.nama_anggota}"

class denda(models.Model) :
    nim_anggota = models.CharField(max_length=12)
    nama_anggota = models.CharField(max_length=100)
    denda = models.CharField(max_length=100 , null=True)

    def __str__(self) -> str:
        return f"{self.nim_anggota}"

class jenis_denda(models.Model) :
    keterangan = models.CharField(max_length=20)
    terlambat = models.DateField(blank=True)

    def __str__(self) -> str:
        return f"{self.keterangan}"

class peminjaman(models.Model) :
     nama_anggota = models.CharField(max_length=100)
     tgl_pinjam = models.DateField(blank=True)
     tgl_kembali = models.DateField(blank=True)
     judul_buku = models.TextField()

     def __str__(self) -> str:
        return f"{self.nama_anggota}"

class petugas(models.Model) :
    nim_petugas = models.CharField(max_length=12)
    nama_petugas = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.nama_petugas}"

class transaksi(models.Model) :
    tgl_denda = models.DateField(blank=True)
    besar_transaksi = models.CharField(max_length=5 , null=True)
    nama_petugas = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.tgl_denda}"