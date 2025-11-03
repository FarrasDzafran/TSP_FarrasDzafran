input("NIM: ")
input("Nama: ")
input("Kelompok: ")
input("Asisten Pembimbing: ")
print(" ")

print("NIM (251093ABCD)")
A=int(input("Masukkan digit A pada NIM: "))
B=int(input("Masukkan digit B pada NIM: "))
C=int(input("Masukkan digit C pada NIM: "))
D=int(input("Masukkan digit D pada NIM: "))
print(" ")

#soal 1
Total_Belanja = A*100000+B*10000+C*1000
print("Total Belanja Pelanggan: Rp",Total_Belanja)

#soal 2 dan 3
if (1<=D<=4):
    Membership_Pelanggan = "Silver"
    BesarDiskon = int(0.05*Total_Belanja)
elif (6<=D<=7):
    Membership_Pelanggan = "Gold"
    BesarDiskon = int(0.1*Total_Belanja)
elif (8<=D<=9):
    Membership_Pelanggan = "Platinum"
    BesarDiskon = int(0.15*Total_Belanja)
elif (D == 0):
    Membership_Pelanggan = "Non-member"
    BesarDiskon = int(0)
else:
    print("Pilihan Tidak Tersedia")

print("Membership Pelanggan: ",Membership_Pelanggan)
print("Besar Diskon: Rp",BesarDiskon)

#soal 4
TotalBelanjaSetelahDiskon = Total_Belanja - BesarDiskon
print("Total Belanja Setelah Diskon: Rp",TotalBelanjaSetelahDiskon)

#soal 5 dan 6
MP = input("Pilih metode pembayaran 1.Tunai, 2. QRIS, 3. Debit: ")
if MP == "1" :
    HargaAkhir = int(TotalBelanjaSetelahDiskon)
    print("Metode Pembayaran Yang Dipilih: Tunai")
elif MP == "2" :
    HargaAkhir = int(TotalBelanjaSetelahDiskon + 2500)
    print("Metode Pembayaran Yang Dipilih: QRIS")
elif MP == "3" :
    HargaAkhir = int(TotalBelanjaSetelahDiskon + 5000)
    print("Metode Pembayaran Yang Dipilih: Debit")
else :
    print("Metode Pembayaran Tidak Tersedia")

print("Total belanja akhir anda: Rp",HargaAkhir)