from django.contrib import admin

from anggota.models import anggota
from buku.models import buku
from daftar_hadir.models import daftar_hadir
from denda.models import denda
from jenis_denda.models import jenis_denda
from peminjaman.models import peminjaman
from petugas.models import petugas
from transaksi.models import transaksi


# Register your models here.
class anggotaadmin(admin.ModelAdmin) :
    list_display = ["nim", "nama", "alamat"]
admin.site.register(anggota,anggotaadmin)

class bukuadmin(admin.ModelAdmin) :
    list_display = ["judul_buku", "kategori"]
admin.site.register(buku,bukuadmin)

class daftaradmin(admin.ModelAdmin) :
    list_display = ["nama", "tgl_kunjungan"]
admin.site.register(daftar_hadir,daftaradmin)

class dendaadmin(admin.ModelAdmin) :
    list_display = ["nim", "nama", "denda"]
admin.site.register(denda,dendaadmin)

class jenisadmin(admin.ModelAdmin) :
    list_display = ["keterangan", "terlambat"]
admin.site.register(jenis_denda,jenisadmin)

class peminjamanadmin(admin.ModelAdmin) :
    list_display = ["nama", "tgl_pinjam", "tgl_kembali", "judul_buku"]
admin.site.register(peminjaman,peminjamanadmin)

class petugasadmin(admin.ModelAdmin) :
    list_display = ["nim", "nama_petugas"]
admin.site.register(petugas,petugasadmin)

class transaksiadmin(admin.ModelAdmin) :
    list_display = ["tgl_denda", "besar_transaksi", "nama_petugas"]
admin.site.register(transaksi,transaksiadmin)
