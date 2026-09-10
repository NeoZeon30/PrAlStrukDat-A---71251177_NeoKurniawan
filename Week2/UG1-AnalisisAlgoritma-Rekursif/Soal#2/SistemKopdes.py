# import ini jangan dihapus/diedit yak
import random


def totalPenjualan(?, ?):
    # kerjakan di sini


def penjualanTertinggi(?, ?):
    # kerjakan di sini


def diAtasRataRata(?, ?):
    # kerjakan di sini


# Program Utama - Jangan dihapus/diedit yak
angka = int(input("NIM: "))
random.seed(angka)

barang = [
    "Beras",
    "Minyak",
    "Gula",
    "Telur",
    "Kopi",
    "Teh"
]

penjualan = {}

for namaBarang in barang:
    penjualan[namaBarang] = random.randint(100, 500)

data = list(penjualan.items())
n = len(data)

print("\n===== Data Penjualan =====")
for namaBarang, jumlah in penjualan.items():
    print(namaBarang, ":", jumlah)

total = totalPenjualan(data, n)
tertinggi = penjualanTertinggi(data, n)
rataRata = total / n
jumlahDiAtasRataRata = diAtasRataRata(penjualan, rataRata)

print("\n===== Hasil Analisis =====")
print("Total penjualan        :", total)
print("Penjualan tertinggi    :", tertinggi[0], "(", tertinggi[1], ")")
print("Rata-rata penjualan    :", round(rataRata, 2))
print("Di atas rata-rata      :", jumlahDiAtasRataRata, "barang")