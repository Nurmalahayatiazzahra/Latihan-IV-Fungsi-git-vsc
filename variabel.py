def cek_genap_ganjil(angka):
    if angka % 2 == 0:
    else:
        return "ganjil"
    def main():
        while true:
            try:
                angka = int(input("masukkan angka(negatif untuk keluar):"))
                if angka < 0:
                    print("program dihentikan.")
                    break
                else:
                    hasil = cek_genap_ganjil(angka)
                    print(f"Angka{angka} adalah {hasil}.")
                except ValueError:
                    print("input tidak valid.silahkan masukkan angka.")
if_name_ == "_main_":
    main()