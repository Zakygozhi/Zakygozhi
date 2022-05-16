
###### PENJUMLAHAN MATRIKS

print ("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print (" PROGRAM PENJUMLAHAN MATRIX 2X2")
print ("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

print("masukkan nilai-nilai matrix 1")
satu1=int(input("b1k1 : "))
satu2=int(input("b1k2 : "))
dua1=int(input("b2k1 : "))
dua2=int(input("b2k2 : "))

print("masukkan nilai-nilai matrix 2")
Satu1=int(input("b1k1 : "))
Satu2=int(input("b1k2 : "))
Dua1=int(input("b2k1 : "))
Dua2=int(input("b2k2 : "))

matrix1 = [
        [satu1, satu2],
        [dua1, dua2],
]
matrix2 = [
        [Satu1, Satu2],
        [Dua1, Dua2],
]

for A in range(0, len(matrix1)):
    for B in range(0, len(matrix1[0])):
        print (matrix1[A][B] + matrix2[A][B], end=' '),
    print('')




###### NOMOR 1

# Cara 1
print("--------------------------------------------\n               ZakyShop\n--------------------------------------------")

print("Berikut list barang yang tersedia beserta harganya")
print("Baju  : Rp. 100.000,00")
print("Celana: Rp. 120.000,00")
print("Sweter: Rp. 150.000,00")
print("Sepatu: Rp. 200.000,00")
print("Topi  : Rp. 70.000,00\n")


while True:
    baju = int(input("Berapa baju yang ingin anda beli? "))
    biayabaju = 100000 * baju

    celana = int(input("Berapa celana yang ingin anda beli? "))
    biayacelana = 120000 * celana

    sweter = int(input("Berapa sweter yang ingin anda beli? "))
    biayasweter = 150000 * sweter

    sepatu = int(input("Berapa sepatu yang ingin anda beli? "))
    biayasepatu = 200000 * sepatu

    topi = int(input("Berapa topi yang ingin anda beli? "))
    biayatopi = 70000 * topi

    print ("\nRincian Pembelian :\n---------------")
    print(f"Anda ingin membeli {baju} buah baju, \n{celana} buah celana, \n{sweter} buah sweter, \n{sepatu} buah sepatu, \ndan {topi} buah topi\n")

    konfirmasi = input("Apakah pesanan anda sudah sesuai? (ya/tidak)\n").lower()

    if konfirmasi == "ya":
        break

print()
total = biayabaju + biayacelana + biayasweter + biayasepatu + biayatopi
print(f"Total belanja anda adalah Rp{total}")

# Cara 2
print("--------------------------------------------\n               Zakymart\n--------------------------------------------")

print("Masukkan nama dan harga barang sesuai price tag")

nama_barang = input("\nmasukkan nama barang :")
harga_satuan = eval(input ("\nmasukkan harga barang sesuai list :"))
jumlah_barang = eval(input ("\nmasukkan jumlah barang :"))
total_harga_barang = harga_satuan*jumlah_barang

print("\nAnda ingin membeli %d %s. Apakah pesanan sudah sesuai ?" %(jumlah_barang,nama_barang))

print("\npilih : Sesuai/Tidak")

pilihan = input(":")

if (pilihan=="Sesuai"):
    print ("\nBerikut Total Pembelian Anda : %d" %(total_harga_barang) )
else :
    print ("\nsilahkan melakukan pemesanan kembali :\n)")




###### Nomor 2

print ("=====================================")
print ("PROGRAM DETEKSI BILANGAN GANJIL/GENAP")
print ("=====================================")

jumlahgenap = 0
jumlahganjil = 0

print ("\nmasukkan angka dengan pemisah koma (',')")
print ("contoh (10, 1, 13, 25, 16, 8, 192)\n")
angka = input("Masukkan angka: ")
angka = angka.split(",")
print(angka)

for i in angka:
    if int(i)%2 == 0:
        jumlahgenap+=1
    else:
        jumlahganjil+=1

print()
print("Jumlah bilangan ganjil adalah", jumlahganjil)
print("Jumlah bilangan genap adalah", jumlahgenap)




###### Nomor 3

print ("\nmasukkan angka dengan pemisah koma (',')")
print ("contoh (10, 1, 13, 25, 16, 8, 192)\n")

bilangan = str(input("Masukkan bilangan: "))
bilangan = bilangan.split(",")

hasil = 0
for i in bilangan:
    i = int(i)
    if i % 3 == 0:
        hasil+=1

print(f"Terdapat {hasil} angka kelipatan tiga yaitu: ")
for i in bilangan:
    i = int(i)
    if i % 3 == 0:
        print(i)



###### Nomor 4

nilai_akhir = int(input("Masukkan Nilai Akhir :"))
for i in range(1,nilai_akhir+1):
    for j in range(1,i+1):
        print(j)
    print()



###### Nomor 5

print("=====================================================================================")
print("                           PROGRAM PENGINPUTAN NILAI") 
print("=====================================================================================")
data = []
while True:
    print("\nApa yang ingin dilakukan?")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Exit")
    pilihan = int(input("Pilihan: "))
    if pilihan == 1:
        print ("\nmasukkan data dengan urutan dan format sebagai berikut :")
        print ("-nama panjang mhs, N.Tugas, N.Kuis, N.UTS, N.UAS-\n")
        print ("*************")
        print ("Bobot nilai :\n N.Tugas(30%) \n N.Kuis(20%) \n N.UTS(25%) \n N.UAS(25%) ")
        print ("*************")
        datamhs = input("Masukkan data: \n")
        datamhs = datamhs.split(",")
        data.append(datamhs)
    elif pilihan == 2:
        print("---------------------------------------------------------------------------------------")
        print("No.      Nama Mhs            N.Tugas    N.Kuis    N.UTS    N.UAS    NilaiAkhir")
        print("---------------------------------------------------------------------------------------")
        count=0        
        for i in (data):
            count+=1
            NilaiAkhir = (((int(i[1]))*30 + int(i[2])*20 + (int(i[3]))*25 + int(i[4])*25))/100
            print (str(count)+".   ", "       ".join(i),"   ", NilaiAkhir)
            print ()
            print ("*Data yang ditampilkan sesuai urutan")
    elif pilihan == 3:
        print("\nTERIMA KASIH!")
    else :
        print ("-Pilihan Tidak Valid-")