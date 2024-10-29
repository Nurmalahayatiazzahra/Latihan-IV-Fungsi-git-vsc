def hitung_gaya_masa():
    print("Pilih opsi yang ingin dihitung:")
    print("1. Hitung Gaya (F)")
    print("2. Hitung Masa (m)")
    print("3. Hitung Percepatan (a)")
    
    pilihan = input("Masukkan pilihan (1/2/3): ")

    if pilihan == '1':
        m = float(input("Masukkan masa (m) dalam kg: "))
        a = float(input("Masukkan percepatan (a) dalam m/s²: "))
        F = m * a
        print(f"Gaya (F) adalah: {F} N")
        
    elif pilihan == '2':
        F = float(input("Masukkan gaya (F) dalam N: "))
        a = float(input("Masukkan percepatan (a) dalam m/s²: "))
        m = F / a
        print(f"Masa (m) adalah: {m} kg")
        
    elif pilihan == '3':
        F = float(input("Masukkan gaya (F) dalam N: "))
        m = float(input("Masukkan masa (m) dalam kg: "))
        a = F / m
        print(f"Percepatan (a) adalah: {a} m/s²")
        
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan fungsi
hitung_gaya_masa()