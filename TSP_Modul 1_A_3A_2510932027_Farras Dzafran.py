input('Nama: ')
input('NIM: ')
input('Kelompok: ')
input('Asisten Pembimbing: ')
print("\n")

be = 1500
bb = 20000
pl = 0.05
ba = 0.02
AB = 20
CD = 27

print(f"Nilai AB: {AB} kWh")
print(f"Nilai CD: {CD} kWh\n")

total = AB + CD
print(f"Total pemakaian kWh dalam 2 bulan: {total} kWh")

Be1 = be*AB
Be2 = be*CD
print(f"Biaya energi bulan pertama: Rp {Be1}")
print(f"Biaya energi bulan kedua: Rp {Be2}")

Bs2b = Be1 + Be2 + 2*bb
print(f"Biaya yang dikeluarkan selama 2 bulan sebelum adanya pajak dan biaya administrasi: Rp {Bs2b}")

Pt2b = (pl*Be1) + (pl*Be2)
print(f"Pajak total yang dikeluarkan pada kedua bulan: Rp {Pt2b}")

Ba = ba*(Be1 + Be2 + Pt2b + 2*bb)
print(f"Biaya administrasi yang dikeluarkan pada kedua bulan: Rp {Ba}")

Tta = Bs2b + Pt2b + Ba
print(f"Total tagihan kedua bulan: Rp {Tta}")