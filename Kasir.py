#Aplikasi Kasir

import sys
total = []

print("----------------")
print("Kasir Desy")
print("----------------")

def daftar_barang():
    print("No | Nama Barang | Harga ")
    print("1 | Downy | 23.000")
    print("2 | Baygon |41.100")
    print("3 | Mamy Poko | 59.000")
    print("4 | Ovaltine | 23.000")
    print("5 | Beras |70.000")
    print("--------------------")
    kode = int(input("Masukkan angka barang : "))
    if kode == 1:
        jumlah1 = int(input("Masukan jumlah barang :"))
        total1 = 23.000 * jumlah1
        total.append(total1)
        tanya()
    elif kode == 2:
        jumlah2 = int(input("Masukkan jumlah barang :"))
        total2 = 41.100 * jumlah2
        total.append(total2)
        tanya()
    elif kode == 3:
        jumlah3 = int(input("Masukkan jumlah barang :"))
        total3 = 59.000 * jumlah3
        total.append(total3)
        tanya()
    elif kode == 4:
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 23.000 * jumlah4
        total.append(total4)
        tanya()
    elif kode == 5 :
        jumlah5 = int(input("Masukkan jumlah barang :"))
        total5 = 70.000 * jumlah5
        total.append(total5)
        tanya()
    return

def tanya ():
    print("\n----------------")
    tanya = input("Ingin tambah barang ? [y/n] :")
    print("---------------------")
    if tanya == "y":
        daftar_barang()
    elif tanya == "n" :
        akhir()
    else: 
        print("Pilihan yang anda masukan salah!")

def akhir ():
    for harga in total :
        print("Subtotal   : ", sum (total))
        diskon = 0
        a = sum (total)
        if a > 500.000:
            diskon = a * 8 /100
        elif a > 300.000:
             diskon = a * 5 /100
        elif a > 200.000 :
            diskon = a * 3 /100
        elif a > 100.000 :
            diskon = a * 1/100
        else :
            diskon = 0
        print ("Potongan Harga : " , diskon)
        totalakhir = a - diskon
        print("Total     :", totalakhir)
        print("--------------------")
        bayar = int(input("Bayar     :"))
        kembalian = bayar = totalakhir
        print("Kembalian :", kembalian)
        print("-----------------------")
        print("Terima Kasih ")
        print("-----------------------")
        
daftar_barang()