# Perhitungan matematika bangun ruang 2D dan 3D

# 2D -- Luas Segitiga
print("Luas segitiga")
alas = int(input("Panjang alas segitiga: "))
tinggi = int(input("Tinggi segitiga: "))
luas_segitiga = (alas * tinggi) / 2
print("Luas Segitiga: ", luas_segitiga)

# 3D -- Volume Tabung
print("\nVolume tabung")
phi = 3.14
r = int(input("Jari-jari alas tabung: "))
t = int(input("Tinggi tabung: "))
volume_tabung = phi * (r ** 2) * t
print("Volume tabung : ", volume_tabung)
              
