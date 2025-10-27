PIN = 2027
salah = 0
while salah < 3:
    pin = int(input("Masukkan PIN admin bioskop: "))
    if pin == PIN:
        print("PIN benar. Silahkan lanjutkan pemesanan.\n")
        while True:

            film = input("Daftar film:\n "
            "1. Harry Potter (Rp 40.000)\n "
            "2. Oppenheimer (Rp 45.000)\n "
            "3. Mencuri Raden Saleh (Rp 40.000)\n "
            "4. One For all (Rp20.000)\n Pilih jenis film:")

            if film == "1":
                Harga = 40000
            elif film == "2":
                Harga = 45000
            elif film == "3":
                Harga = 30000
            elif film == "4":
                Harga = 20000
            else:
                print("Pilihan tidak tersedia, pilih ulang\n")
                continue
            JTiket = int(input("\nMasukkan jumlah tiket: "))
            Harga_Bayar = Harga*JTiket
            print("Total harga tiket anda: Rp",Harga_Bayar)
            Ulang = input("Apakah ingin melakukan transaksi lagi?(Ya/Tidak) ").lower()
            if Ulang == "ya":
                continue
            elif Ulang == "tidak":
                print("Transaksi selesai")
                break
        break
    else:
        salah += 1
        print(f"PIN salah! Kesalahan {salah}/3.")
        if salah == 3:
            print("Anda telah 3x salah PIN. Program dihentikan.")
            break