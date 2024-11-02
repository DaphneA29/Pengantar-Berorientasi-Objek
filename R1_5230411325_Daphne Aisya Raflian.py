
class Produk:
    def __init__(self, kode_produk, nama_produk, jenis_produk, harga):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk
        self.harga = harga

    def display_info(self):
        return f"Produk: {self.nama_produk} (Kode: {self.kode_produk}, Jenis: {self.jenis_produk}, Harga: Rp{self.harga})"


class Snack(Produk):
    def __init__(self, kode_produk, nama_produk, harga):
        super().__init__(kode_produk, nama_produk, 'Snack', harga)

    def display_info(self):  
        return f"Snack: {self.nama_produk} - Harga: Rp{self.harga}"


class Makanan(Produk):
    def __init__(self, kode_produk, nama_produk, harga):
        super().__init__(kode_produk, nama_produk, 'Makanan', harga)

    def display_info(self):  
        return f"Makanan: {self.nama_produk} - Harga: Rp{self.harga}"


class Minuman(Produk):
    def __init__(self, kode_produk, nama_produk, harga):
        super().__init__(kode_produk, nama_produk, 'Minuman', harga)

    def display_info(self): 
        return f"Minuman: {self.nama_produk} - Harga: Rp{self.harga}"


class Pegawai:
    def __init__(self, nik, nama, alamat):
        self.nik = nik
        self.nama = nama
        self.alamat = alamat

    def display_info(self):
        return f"NIK: {self.nik}, Nama: {self.nama}, Alamat: {self.alamat}"



produk_list = [
    Snack('S256', 'Keripik Kentang', 15000),
    Snack('S239', 'Keripik Bawang', 15000),
    Snack('S287', 'Keripik Kentang', 15000),    
    Makanan('M393', 'Nasi Goreng', 20500),
    Makanan('M398', 'Mie Goreng', 25000),
    Makanan('M345', 'Kwetiau Seafood', 25000),
    Minuman('D445', 'Teh Manis', 5000),
    Minuman('D476', 'Es Jeruk', 7000),
    Minuman('D489', 'Es Kopi Susu', 10000),
]

pegawai_list = []


def main_menu():
    while True:
        print("\n=== Menu Program ===")
        print("1. Tambah Data Pegawai")
        print("2. Lihat Data Pegawai")
        print("3. Lihat Daftar Produk")
        print("4. Buat Transaksi")
        print("5. Keluar")

        pilihan = input("Pilih =^_^= : ")

        if pilihan == '1':
            tambah_pegawai()
        elif pilihan == '2':
            lihat_pegawai()
        elif pilihan == '3':
            tampilkan_menu_produk()
        elif pilihan == '4':
            buat_transaksi()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan program ini. =^.^= !!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def tambah_pegawai():
    nik = input("Masukkan NIK pegawai: ")
    nama = input("Masukkan nama pegawai: ")
    alamat = input("Masukkan alamat pegawai: ")
    pegawai = Pegawai(nik, nama, alamat)
    pegawai_list.append(pegawai)
    print("Data pegawai berhasil ditambahkan. ^_^ !")

def lihat_pegawai():
    if not pegawai_list:
        print("Belum ada data pegawai. T_T ")
    else:
        print("\n=== Data Pegawai ===")
        for pegawai in pegawai_list:
            print(pegawai.display_info())

def tampilkan_menu_produk():
    print("\n=== Daftar Produk ===")
    for i, produk in enumerate(produk_list, 1):
        print(f"{i}. {produk.display_info()}")

def buat_transaksi():
    if not pegawai_list:
        print("Tidak ada pegawai T_T. Silakan tambahkan data pegawai terlebih dahulu ^_^ !")
        return

    nama_pegawai = input("\nMasukkan nama pegawai yang melakukan transaksi: ")
    pegawai = next((p for p in pegawai_list if p.nama == nama_pegawai), None)
    if not pegawai:
        print("Pegawai tidak ditemukan. Silakan coba lagi ^_^ !")
        return

    tampilkan_menu_produk()
    nomor = int(input("Pilih nomor produk (0 untuk batal): "))

    if nomor == 0:
        print("Transaksi dibatalkan. T_T")
        return
    elif 1 <= nomor <= len(produk_list):
        produk = produk_list[nomor - 1]
        jumlah = int(input(f"Masukkan jumlah {produk.nama_produk} yang dibeli: "))
        total_harga = produk.harga * jumlah

        print("\n=== Nota Pembelian ===")
        print(f"Nama Pegawai : {pegawai.nama}")
        
        print(f"Produk       : {produk.nama_produk}")
        
        print(f"Jumlah       : {jumlah}")
        
        print(f"Harga Satuan : Rp{produk.harga}")
        
        print(f"Total Harga          : Rp{total_harga}")
        print("======================")
        print("Transaksi berhasil dibuat!")
    else:
        print("Nomor produk tidak valid.")

# Menjalankan program
main_menu()
