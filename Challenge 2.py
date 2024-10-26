def menu():
    while True:
        print("=== Cek Bilangan ===")
        print("|1) Bilangan Prima  |")
        print("|2) Bilangan Ganjil |")
        print("|3) Bilangan Genap  |")
        print("|4) Keluar          |")
        
        pilihan = input("=== Pilihan Menu: ")

        if pilihan == '1':
            cek_prima()
        elif pilihan == '2':
            cek_ganjil()
        elif pilihan == '3':
            cek_genap()
        elif pilihan == '4':
            print("Program selesai!")
            break
        else:
            print("Pilihan tidak valid.")
        
def cek_prima():
    awal = int(input("Bilangan awal: "))
    akhir = int(input("Bilangan akhir: "))
    print("Bilangan Prima dari {awal} hingga {akhir}:")
    for angka in range(awal, akhir + 1):
        if angka < 2:
            continue
        is_prima = True
        for i in range(2, int(angka**0.5) + 1):
            if angka % i == 0:
                is_prima = False
                break
        if is_prima:
            print(angka, end=" ")
    print()

def cek_ganjil():
    awal = int(input("Bilangan awal: "))
    akhir = int(input("Bilangan akhir: "))
    print(f"Bilangan Ganjil dari {awal} hingga {akhir}:")
    for angka in range(awal, akhir + 1):
        if angka % 2 != 0:
            print(angka, end=" ")
    print()
    
def cek_genap():
    awal = int(input("Bilangan awal: "))
    akhir = int(input("Bilangan akhir: "))
    print(f"Bilangan Ganjil dari {awal} hingga {akhir}:")
    for angka in range(awal, akhir + 1):
        if angka % 2 != 0:
            print(angka, end=" ")
    print()    


menu()        
        
        

    

    
    