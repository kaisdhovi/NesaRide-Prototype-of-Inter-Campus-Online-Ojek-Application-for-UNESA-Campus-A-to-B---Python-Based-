# Class User
class User:
    def __init__(self, user_id, nama):
        self.user_id = user_id
        self.nama = nama
        self.pembelian_obat_list = []
        self.konsultasi_list = []

    def tambah_pembelian_obat(self, pembelian_obat):
        self.pembelian_obat_list.append(pembelian_obat)

    def tambah_konsultasi(self, konsultasi):
        self.konsultasi_list.append(konsultasi)

# Class Obat
class Obat:
    def __init__(self, obat_id, nama, harga, stok):
        self.obat_id = obat_id
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def kurangi_stok(self, jumlah):
        if self.stok >= jumlah:
            self.stok -= jumlah
        else:
            raise ValueError("Stok tidak mencukupi")

# Class DetailPembelian (Class Asosiasi)
class DetailPembelian:
    def __init__(self, pembelian_obat, obat, jumlah):
        self.pembelian_obat = pembelian_obat
        self.obat = obat
        self.jumlah = jumlah
        self.total_harga = jumlah * obat.harga
        self.obat.kurangi_stok(jumlah)  # Kurangi stok obat saat dibeli

# Class PembelianObat
class PembelianObat:
    def __init__(self, pembelian_id, tanggal):
        self.pembelian_id = pembelian_id
        self.tanggal = tanggal
        self.detail_pembelian_list = []

    def tambah_detail_pembelian(self, detail_pembelian):
        self.detail_pembelian_list.append(detail_pembelian)

    def hitung_total_harga(self):
        total = sum([detail.total_harga for detail in self.detail_pembelian_list])
        return total

# Class Dokter
class Dokter:
    def __init__(self, dokter_id, nama):
        self.dokter_id = dokter_id
        self.nama = nama

# Class Konsultasi
class Konsultasi:
    def __init__(self, konsultasi_id, dokter, tanggal, user):
        self.konsultasi_id = konsultasi_id
        self.dokter = dokter
        self.tanggal = tanggal
        self.user = user

# Class Admin
class Admin:
    def __init__(self, admin_id, nama):
        self.admin_id = admin_id
        self.nama = nama

    def akses_riwayat_transaksi(self, user):
        return user.pembelian_obat_list

    def update_stok_obat(self, obat, stok_baru):
        obat.stok = stok_baru

# Simulasi Data Sementara
# Buat beberapa user, dokter, dan obat

user1 = User(1, "Andi")
user2 = User(2, "Budi")
dokter1 = Dokter(1, "Dr. Siti")
obat1 = Obat(1, "Paracetamol", 5000, 100)
obat2 = Obat(2, "Amoxicillin", 10000, 50)

# Pembelian obat oleh user1
pembelian1 = PembelianObat(1, "2024-10-06")
detail1 = DetailPembelian(pembelian1, obat1, 2)  # Beli 2 Paracetamol
detail2 = DetailPembelian(pembelian1, obat2, 3)  # Beli 3 Amoxicillin

pembelian1.tambah_detail_pembelian(detail1)
pembelian1.tambah_detail_pembelian(detail2)

user1.tambah_pembelian_obat(pembelian1)

# Konsultasi oleh user2 dengan dokter1
konsultasi1 = Konsultasi(1, dokter1, "2024-10-08", user2)
user2.tambah_konsultasi(konsultasi1)

# Admin mengakses riwayat transaksi user1
admin1 = Admin(1, "Admin1")
riwayat_transaksi_user1 = admin1.akses_riwayat_transaksi(user1)

# Cetak total harga pembelian user1
print(f"Total harga pembelian oleh {user1.nama}: {pembelian1.hitung_total_harga()}")

# Cetak riwayat transaksi user1
print("Riwayat transaksi user1:")
for pembelian in riwayat_transaksi_user1:
    print(f"ID Pembelian: {pembelian.pembelian_id}, Tanggal: {pembelian.tanggal}, Total Harga: {pembelian.hitung_total_harga()}")

# Cetak detail konsultasi user2
print(f"User {user2.nama} melakukan konsultasi dengan {konsultasi1.dokter.nama} pada tanggal {konsultasi1.tanggal}")
