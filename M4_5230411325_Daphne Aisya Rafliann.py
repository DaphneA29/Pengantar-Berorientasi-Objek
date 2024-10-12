class ManajemenDebitur:
    def __init__(self):
        self.daftar_debitur = []

    def tambah_debitur(self, nama, nomor_ktp, batas_pinjaman):
        for debitur in self.daftar_debitur:
            if debitur['ktp'] == nomor_ktp:
                print("KTP sudah terdaftar, tambah debitur gagal !!")
                print("==============================")
                return
        self.daftar_debitur.append({
            'nama': nama,
            'ktp': nomor_ktp,
            'batas_pinjaman': batas_pinjaman,
            'riwayat_pinjaman': []
        })
        print("Debitur baru berhasil ditambahkan.")
        print("==============================")

    def cari_debitur(self, nama):
        for debitur in self.daftar_debitur:
            if debitur['nama'] == nama:
                print("============================")
                print(f"Nama: {debitur['nama']}")
                print(f"KTP: {debitur['ktp']}")
                print(f"Batas Pinjaman: {debitur['batas_pinjaman']}")
                print("============================")
                return debitur
        print("Debitur tidak ditemukan !!")
        return None

    def tampilkan_seluruh_debitur(self):
        if not self.daftar_debitur:
            print("Belum ada debitur yang terdaftar !!")
            print("===============================")
            return
        for debitur in self.daftar_debitur:
            print("================================")
            print(f"Nama: {debitur['nama']}")
            print(f"KTP: {debitur['ktp']}")
            print(f"Batas Pinjaman: {debitur['batas_pinjaman']}")
            print("================================")


class ManajemenPinjaman:
    def ajukan_pinjaman(self, debitur, jumlah_pinjaman, bunga, lama_angsuran):
        if jumlah_pinjaman > debitur['batas_pinjaman']:
            print("Pinjaman melebihi batas yang ditetapkan !!")
            print("==============================")
            return
        pokok_angsuran = jumlah_pinjaman * (bunga / 100)
        angsuran_bulanan = pokok_angsuran / lama_angsuran
        total_angsuran = pokok_angsuran + angsuran_bulanan

        debitur['riwayat_pinjaman'].append({
            'jumlah_pinjaman': jumlah_pinjaman,
            'bunga': bunga,
            'lama_angsuran': lama_angsuran,
            'pokok_angsuran': pokok_angsuran,
            'angsuran_bulanan': angsuran_bulanan,
            'total_angsuran': total_angsuran
        })
        print("Pinjaman berhasil ditambahkan.")
        print("==============================")

    def lihat_pinjaman(self, debitur):
        if not debitur['riwayat_pinjaman']:
            print(f"Belum ada pinjaman untuk debitur {debitur['nama']}.")
            return
        for pinjaman in debitur['riwayat_pinjaman']:
            print("================================")
            print(f"Nama: {debitur['nama']}")
            print(f"Pinjaman: {pinjaman['jumlah_pinjaman']}")
            print(f"Bunga: {pinjaman['bunga']}%")
            print(f"Lama Angsuran: {pinjaman['lama_angsuran']} bulan")
            print(f"Pokok Angsuran: {pinjaman['pokok_angsuran']}")
            print(f"Angsuran Bulanan: {pinjaman['angsuran_bulanan']}")
            print(f"Total Angsuran: {pinjaman['total_angsuran']}")
            print("================================")


def jalankan_aplikasi():
    kelola_debitur = ManajemenDebitur()
    kelola_pinjaman = ManajemenPinjaman()

    while True:
        print(" - - - - - PINJOL - - - - -")
        print("1. Kelola Debitur")
        print("2. Kelola Pinjaman")
        print("3. Keluar")
        print("---------------------------")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            while True:
                print("1. Tambah Debitur Baru")
                print("2. Cari Debitur")
                print("3. Lihat Semua Debitur")
                print("4. Kembali")

                sub_pilihan = input("Pilih menu: ")

                if sub_pilihan == "1":
                    nama = input("Masukkan Nama Debitur: ")
                    nomor_ktp = input("Masukkan KTP Debitur: ")
                    batas_pinjaman = int(input("Masukkan Batas Pinjaman: "))
                    kelola_debitur.tambah_debitur(nama, nomor_ktp, batas_pinjaman)

                elif sub_pilihan == "2":
                    nama = input("Masukkan Nama Debitur: ")
                    kelola_debitur.cari_debitur(nama)

                elif sub_pilihan == "3":
                    kelola_debitur.tampilkan_seluruh_debitur()

                elif sub_pilihan == "4":
                    break
                else:
                    print("Pilihan tidak valid.")

        elif pilihan == "2":
            while True:
                print("1. Ajukan Pinjaman")
                print("2. Lihat Pinjaman")
                print("3. Kembali")

                sub_pilihan = input("Pilih menu: ")

                if sub_pilihan == "1":
                    nama = input("Masukkan Nama Debitur: ")
                    debitur = kelola_debitur.cari_debitur(nama)
                    if debitur:
                        jumlah_pinjaman = int(input("Masukkan Jumlah Pinjaman: "))
                        bunga = int(input("Masukkan Bunga (%): "))
                        lama_angsuran = int(input("Masukkan Lama Angsuran (bulan): "))
                        kelola_pinjaman.ajukan_pinjaman(debitur, jumlah_pinjaman, bunga, lama_angsuran)

                elif sub_pilihan == "2":
                    nama = input("Masukkan Nama Debitur: ")
                    debitur = kelola_debitur.cari_debitur(nama)
                    if debitur:
                        kelola_pinjaman.lihat_pinjaman(debitur)

                elif sub_pilihan == "3":
                    break
                else:
                    print("Pilihan tidak valid.")

        elif pilihan == "3":
            break
        else:
            print("Menu tidak tersedia.")


if __name__ == "__main__":
    jalankan_aplikasi()
