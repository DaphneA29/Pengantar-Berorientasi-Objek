import mysql.connector

# Membuat koneksi ke database
try:
    conn = mysql.connector.connect(
        user="root",
        host="localhost",
        password="", 
        database="Penjualan"
    )
    cur = conn.cursor()

    # Membuat database jika belum ada
    cur.execute("CREATE DATABASE IF NOT EXISTS Penjualan;")
    print("Database 'Penjualan' siap atau sudah ada.")

    # Membuat tabel jika belum ada
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Pegawai (
        NIK CHAR(4) NOT NULL PRIMARY KEY,
        Nama VARCHAR(50),
        Alamat VARCHAR(255)
    )
    """)
    print("Tabel 'Pegawai' berhasil dibuat atau sudah ada.")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS Produk (
        Kode_Produk CHAR(4) NOT NULL PRIMARY KEY,
        Nama_Produk VARCHAR(50),
        Jenis_Produk VARCHAR(50),
        Harga INT
    )
    """)
    print("Tabel 'Produk' berhasil dibuat atau sudah ada.")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS Transaksi (
        No_Transaksi CHAR(20) NOT NULL PRIMARY KEY,
        Detail_Transaksi VARCHAR(255),
        Nama VARCHAR(50),
        Kode_Produk CHAR(4),
        FOREIGN KEY (Nama) REFERENCES Pegawai(Nama),
        FOREIGN KEY (Kode_Produk) REFERENCES Produk(Kode_Produk)
    )
    """)

    print("Tabel 'Transaksi' berhasil dibuat atau sudah ada.")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS Struk (
        No_Transaksi CHAR(4),
        Nama_Pegawai VARCHAR(50),
        Nama_Produk VARCHAR(50),  
        Jumlah_Produk INT,
        Total_Harga INT,
        FOREIGN KEY (No_Transaksi) REFERENCES Transaksi(No_Transaksi)
    )
    """)
    print("Tabel 'Struk' berhasil dibuat atau sudah ada.")

    # Menambahkan satu data awal ke tabel Produk
    cur.execute("""
    INSERT IGNORE INTO Produk (Kode_Produk, Nama_Produk, Jenis_Produk, Harga)
    VALUES ('Z01', 'Kopi', 'Minuman', 35000)
    """)
    conn.commit()
    print("Data produk awal berhasil ditambahkan.")


    # Menu aplikasi
    def menu():
        while True:
            print("\n=== Menu Aplikasi ===")
            print("1. Tambah Produk")
            print("2. Hapus Produk")
            print("3. Tampilkan Produk")
            print("4. Keluar")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                tambah_produk()
            elif pilihan == "2":
                hapus_produk()
            elif pilihan == "3":
                tampilkan_produk()
            elif pilihan == "4":
                print("Keluar dari aplikasi.")
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")

    def tambah_produk():
        print("\n=== Tambah Produk ===")
        kode_produk = input("Masukkan kode produk: ")
        nama_produk = input("Masukkan nama produk: ")
        jenis_produk = input("Masukkan jenis produk: ")
        harga = int(input("Masukkan harga produk: "))
        cur.execute("""
            INSERT INTO Produk (Kode_Produk, Nama_Produk, Jenis_Produk, Harga)
            VALUES (%s, %s, %s, %s)
        """, (kode_produk, nama_produk, jenis_produk, harga))
        conn.commit()
        print("Produk berhasil ditambahkan!")

    def hapus_produk():
        print("\n=== Hapus Produk ===")
        kode_produk = input("Masukkan kode produk yang ingin dihapus: ")
        cur.execute("""
            DELETE FROM Produk WHERE Kode_Produk = %s
        """, (kode_produk,))
        conn.commit()
        print("Produk berhasil dihapus!")

    def tampilkan_produk():
        print("\n=== Daftar Produk ===")
        cur.execute("SELECT * FROM Produk")
        result = cur.fetchall()
        if not result:
            print("Belum ada produk yang terdaftar.")
        else:
            for row in result:
                print(f"Kode: {row[0]}, Nama: {row[1]}, Jenis: {row[2]}, Harga: {row[3]}")

    # Menjalankan menu
    if _name_ == "_main_":
        menu()

except mysql.connector.Error as err:
    print(f"Error: {err}")
