# Definisi Class
class User:
    def __init__(self, user_id, nama):
        self.user_id = user_id
        self.nama = nama
        self.pembelian_obat_list = []
        self.konsultasi_list = []

    def tambah_pembelian_obat(self, pembelian):
        self.pembelian_obat_list.append(pembelian)

    def tambah_konsultasi(self, konsultasi):
        self.konsultasi_list.append(konsultasi)


class Admin:
    def __init__(self, admin_id, nama):
        self.admin_id = admin_id
        self.nama = nama

    def akses_riwayat_transaksi(self, user):
        return user.pembelian_obat_list

    def update_stok_obat(self, obat, stok_baru):
        obat.stok = stok_baru


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
            print(f"Stok {self.nama} tidak mencukupi.")


class PembelianObat:
    def __init__(self, pembelian_id, tanggal):
        self.pembelian_id = pembelian_id
        self.tanggal = tanggal
        self.detail_pembelian_list = []

    def tambah_detail_pembelian(self, detail):
        self.detail_pembelian_list.append(detail)

    def hitung_total_harga(self):
        total = 0
        for detail in self.detail_pembelian_list:
            total += detail.harga_total()
        return total


class DetailPembelian:
    def __init__(self, pembelian, obat, jumlah):
        self.pembelian = pembelian
        self.obat = obat
        self.jumlah = jumlah

    def harga_total(self):
        return self.obat.harga * self.jumlah


class Dokter:
    def __init__(self, dokter_id, nama):
        self.dokter_id = dokter_id
        self.nama = nama


class Konsultasi:
    def __init__(self, konsultasi_id, dokter, tanggal, user):
        self.konsultasi_id = konsultasi_id
        self.dokter = dokter
        self.tanggal = tanggal
        self.user = user


# Fungsi untuk login
def login(users, admins):
    print("===== LOGIN =====")
    username = input("Username: ")
    password = input("Password: ")

    # Cek apakah User atau Admin
    for user in users:
        if user['username'] == username and user['password'] == password:
            print(f"Selamat datang, {user['nama']}!")
            return "user", user['user_object']
    for admin in admins:
        if admin['username'] == username and admin['password'] == password:
            print(f"Selamat datang, {admin['nama']} (Admin)!")
            return "admin", admin['admin_object']

    print("Username atau password salah!")
    return None, None


# Fungsi untuk user memilih fitur
def user_menu(user):
    while True:
        print("\n===== MENU USER =====")
        print("1. Beli Obat")
        print("2. Konsultasi dengan Dokter")
        print("3. Lihat Riwayat Pembelian Obat")
        print("4. Keluar")
        pilihan = input("Pilih: ")

        if pilihan == "1":
            beli_obat(user)
        elif pilihan == "2":
            konsultasi(user)
        elif pilihan == "3":
            lihat_riwayat_pembelian(user)
        elif pilihan == "4":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid!")


# Fungsi untuk admin memilih fitur
def admin_menu(admin):
    while True:
        print("\n===== MENU ADMIN =====")
        print("1. Akses Riwayat Transaksi User")
        print("2. Update Stok Obat")
        print("3. Keluar")
        pilihan = input("Pilih: ")

        if pilihan == "1":
            akses_riwayat(admin)
        elif pilihan == "2":
            update_stok(admin)
        elif pilihan == "3":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid!")


# Fungsi untuk beli obat
def beli_obat(user):
    print("\n===== BELI OBAT =====")
    pembelian = PembelianObat(len(user.pembelian_obat_list) + 1, "2024-10-06")

    while True:
        obat_id = input("Masukkan ID Obat (atau 'selesai' untuk mengakhiri): ")
        if obat_id == "selesai":
            break
        jumlah = int(input("Jumlah yang dibeli: "))

        # Cari obat berdasarkan ID (misal: obat1 dan obat2 di database)
        if obat_id == "1":
            obat = obat1
        elif obat_id == "2":
            obat = obat2
        else:
            print("Obat tidak ditemukan!")
            continue

        # Tambahkan obat ke detail pembelian
        detail_pembelian = DetailPembelian(pembelian, obat, jumlah)
        pembelian.tambah_detail_pembelian(detail_pembelian)

    user.tambah_pembelian_obat(pembelian)
    print(f"Total harga pembelian: {pembelian.hitung_total_harga()}")


# Fungsi untuk konsultasi
def konsultasi(user):
    print("\n===== KONSULTASI =====")
    dokter_id = input("Masukkan ID Dokter: ")

    # Cari dokter berdasarkan ID (misal: dokter1 di database)
    if dokter_id == "1":
        dokter = dokter1
    else:
        print("Dokter tidak ditemukan!")
        return

    tanggal = input("Masukkan tanggal konsultasi (YYYY-MM-DD): ")
    konsultasi_baru = Konsultasi(len(user.konsultasi_list) + 1, dokter, tanggal, user)
    user.tambah_konsultasi(konsultasi_baru)

    print(f"Konsultasi dijadwalkan dengan {dokter.nama} pada {tanggal}")


# Fungsi untuk melihat riwayat pembelian obat user
def lihat_riwayat_pembelian(user):
    print("\n===== RIWAYAT PEMBELIAN OBAT =====")
    for pembelian in user.pembelian_obat_list:
        print(f"ID Pembelian: {pembelian.pembelian_id}, Tanggal: {pembelian.tanggal}, Total Harga: {pembelian.hitung_total_harga()}")


# Fungsi untuk admin mengakses riwayat transaksi
def akses_riwayat(admin):
    print("\n===== AKSES RIWAYAT TRANSAKSI USER =====")
    user_id = int(input("Masukkan ID User: "))

    # Cari user berdasarkan ID
    if user_id == 1:
        riwayat = admin.akses_riwayat_transaksi(user1)
    elif user_id == 2:
        riwayat = admin.akses_riwayat_transaksi(user2)
    else:
        print("User tidak ditemukan!")
        return

    for pembelian in riwayat:
        print(f"ID Pembelian: {pembelian.pembelian_id}, Tanggal: {pembelian.tanggal}, Total Harga: {pembelian.hitung_total_harga()}")


# Fungsi untuk admin mengupdate stok obat
def update_stok(admin):
    print("\n===== UPDATE STOK OBAT =====")
    obat_id = input("Masukkan ID Obat: ")
    stok_baru = int(input("Masukkan stok baru: "))

    if obat_id == "1":
        admin.update_stok_obat(obat1, stok_baru)
        print(f"Stok {obat1.nama} telah diperbarui menjadi {obat1.stok}")
    elif obat_id == "2":
        admin.update_stok_obat(obat2, stok_baru)
        print(f"Stok {obat2.nama} telah diperbarui menjadi {obat2.stok}")
    else:
        print("Obat tidak ditemukan!")


# Definisikan beberapa user, dokter, dan obat terlebih dahulu
user1 = User(1, "Andi")
user2 = User(2, "Budi")
admin1 = Admin(1, "Admin1")

dokter1 = Dokter(1, "Dr. Siti")
obat1 = Obat(1, "Paracetamol", 5000, 100)
obat2 = Obat(2, "Amoxicillin", 10000, 50)

# Simulasi login user dan admin
users = [
    {'username': 'andi', 'password': '123', 'nama': 'Andi', 'user_object': user1},
    {'username': 'budi', 'password': '456', 'nama': 'Budi', 'user_object': user2},
]

admins = [
    {'username': 'admin1', 'password': 'adminpass', 'nama': 'Admin1', 'admin_object': admin1},
]

start=login('andi','andiadmin1')