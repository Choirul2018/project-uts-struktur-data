from prettytable import PrettyTable                 #Import library untuk membuat tabel

#Deklarasi Data pemain 
list = [["Jordi Amat", 4, 31, "DF", "Johor Darul Ta'zim"], 
        ["Ernando Ari", 21, 22, "GK", "Persebaya"],
        ["Asnawi Mangkualam", 14, 24, "DF", "Jeonnam Dragon"],
        ["Marselino Ferdinand", 24, 19, "MF", "KMSK Deinze"],
        ["Egy Maulana Vikri", 10, 22, "MF", "Dewa United"],
        ["Marc Klok", 23, 27, "MF", "Persib Bandung"],
        ["Ramadhan Sananta", 9, 21, "ST", "Persis Solo"],
        ["Dendy Sulistyawan", 11, 29, "ST", "Bhayangkara FC"]]

def tambahkanData(arr): # Fungsi tambah data
    data = [] # Array simpan data (penampung)
    nm = str(input("Masukkan Nama Pemain        : ")) # Input Nama
    np = int(input("Masukkan No Punggung Pemain : ")) # Input Nomor punggung
    us = int(input("Masukkan Usia Pemain        : ")) # Input Usia pemain
    ps = str(input("Masukkan Posisi Pemain      : ")) # Input Posisi pemain
    ak = str(input("Masukkan Asal Klub Pemain   : ")) # Input Klub pemain
    print() 
    data.append(nm) # Memasukkan inputan kedalam array penampung
    data.append(np) # Memasukkan inputan kedalam array penampung
    data.append(us) # Memasukkan inputan kedalam array penampung
    data.append(ps) # Memasukkan inputan kedalam array penampung
    data.append(ak) # Memasukkan inputan kedalam array penampung
    arr.append(data)    # Memasukkan array penampung kedalam array data pemain
    print("Data Berhasil Ditambahkan")
    print()

def tampilkanData(arr): # Fungsi tampil data 
    if len(arr) == 0:               # Jika list kosong, Maka tampil "Data Masih Kosong"
        print("Data Masih Kosong")  
    else:                           # Jika terdapat data, Maka menampilkan tabel daftar data pemain
        table = PrettyTable(["Nama", "No Punggung", "Usia", "Posisi", "Asal Klub"]) 
        for i in range(0, len(list)):       # Perulangan sesuai panjang data
            table.add_row(list[i])          # Menampilkan data sesuai indeks
    print(table)                            # Menampilkan Tabel
    print()

def sisipkanData(arr, baris):               # fungsi menyisipkan data 
    data = []                               # Array simpan data (penampung)
    nm = str(input("Masukkan Nama Pemain        : ")) # Input Nama
    np = int(input("Masukkan No Punggung Pemain : ")) # Input Nomor punggung
    us = int(input("Masukkan Usia Pemain        : ")) # Input Usia pemain
    ps = str(input("Masukkan Posisi Pemain      : ")) # Input Posisi pemain
    ak = str(input("Masukkan Asal Klub Pemain   : ")) # Input Klub pemain
    print()
    data.append(nm) # Memasukkan inputan kedalam array penampung
    data.append(np) # Memasukkan inputan kedalam array penampung
    data.append(us) # Memasukkan inputan kedalam array penampung
    data.append(ps) # Memasukkan inputan kedalam array penampung
    data.append(ak) # Memasukkan inputan kedalam array penampung
    arr.insert(baris-1, data) # Memasukkan array penampung kedalam array data pemain sesuai baris yang diinputkan
    print("Data Berhasil Ditambahkan")
    print()
    
def sequentialSearch(arr, item):            # Fungsi Cari data
    hasil = []                              # Array penampung indeks jika tabel ditemukan
    table = PrettyTable(["Nama", "No Punggung", "Usia", "Posisi", "Asal Klub"]) 
    for x in range(0, len(arr)):            # Perulangan sesuai banyaknya data
        for y in range(0, len(arr[x])):     # Perulangan sesuai panjang array
            if item == arr[x][y]:           # Jika Item sesuai dengan data yang dicari
                if x not in hasil:          # Maka akan diperiksa apakah indeks data sudah ada di array penampung atau belum
                    hasil.append(x)         # Jika belum, maka akan dimasukkan kedalam array penampung
    if len(hasil) == 0:                     # Jika array penampung kosong
        print("Data Tidak Ditemukan")       # Maka tampil "Data Masih Kosong"
    else:                                   # Jika terdapat data pada array penampung
        for data in hasil:                  # Maka tampil data yang di cari
            table.add_row(list[data])       
    print(table)                            # Menampilkan Tabel
    print()
      
def shellSort(arr, order, pil):             # Fungsi Pengurutan data                     
    banyakData = len(arr)                   # Menentukan Panjang Data
    interval = banyakData // 2              # Menentukan Batas Tengah
    if pil == True :                        # Jika parameter pil diisi true maka akan masuk kedalam ascending
        while interval > 0: 
            for i in range(interval, banyakData):
                temp1 = arr[i][0]
                temp2 = arr[i][1]
                temp3 = arr[i][2]
                temp4 = arr[i][3]
                temp5 = arr[i][4]
                j = i
                if order == 1:              # jika parameter order diisi 1, maka diurukan sesuai nama
                    banding = temp1
                    indek = 0
                if order == 2:              # jika parameter order diisi 2, maka diurukan sesuai nopung
                    banding = temp2
                    indek = 1
                if order == 3:              # jika parameter order diisi 3, maka diurukan sesuai usia
                    banding = temp3
                    indek = 2
                if order == 4:              # jika parameter order diisi 4, maka diurukan sesuai posisi
                    banding = temp4
                    indek = 3
                if order == 5:              # jika parameter order diisi 5, maka diurukan sesuai asal klub
                    banding = temp5
                    indek = 4
                while j >= interval and arr[j - interval][indek] > banding:         # Proses pengurutan menggunakan shell sort
                    arr[j][0] = arr[j - interval][0]
                    arr[j][1] = arr[j - interval][1]
                    arr[j][2] = arr[j - interval][2]
                    arr[j][3] = arr[j - interval][3]
                    arr[j][4] = arr[j - interval][4]
                    j -= interval
                arr[j][0] = temp1
                arr[j][1] = temp2
                arr[j][2] = temp3
                arr[j][3] = temp4
                arr[j][4] = temp5
            interval //= 2
    else:                                   # Jika parameter pil diisi false maka akan masuk kedalam descending
        while interval > 0:
            for i in range(interval, banyakData):
                temp1 = arr[i][0]
                temp2 = arr[i][1]
                temp3 = arr[i][2]
                temp4 = arr[i][3]
                temp5 = arr[i][4]
                j = i
                if order == 1:              # jika parameter order diisi 1, maka diurukan sesuai nama
                    banding = temp1
                    indek = 0
                if order == 2:              # jika parameter order diisi 2, maka diurukan sesuai nopung
                    banding = temp2
                    indek = 1
                if order == 3:              # jika parameter order diisi 3, maka diurukan sesuai usia
                    banding = temp3
                    indek = 2
                if order == 4:              # jika parameter order diisi 4, maka diurukan sesuai posisi
                    banding = temp4
                    indek = 3
                if order == 5:              # jika parameter order diisi 5, maka diurukan sesuai asal klub
                    banding = temp5         
                    indek = 4
                while j >= interval and arr[j - interval][indek] < banding:         # Proses pengurutan menggunakan shell sort
                    arr[j][0] = arr[j - interval][0]
                    arr[j][1] = arr[j - interval][1]
                    arr[j][2] = arr[j - interval][2]
                    arr[j][3] = arr[j - interval][3]
                    arr[j][4] = arr[j - interval][4]
                    j -= interval
                arr[j][0] = temp1
                arr[j][1] = temp2
                arr[j][2] = temp3
                arr[j][3] = temp4
                arr[j][4] = temp5
            interval //= 2

def ubahData(arr, item):                    # Fungsi Mengubah data
    found = []                              # Array penampung data jika kata kunci ditemukan
    for x in range(0, len(arr)):            # Perulangan sesuai banyaknya data
        if item == arr[x][0]:               # Jika kata kunci sesuai dengan data
            found.append(x)                 # Maka memasukkan indeks data kedalam array penampung
            print("Kata Kunci Ditemukan")
            print()
            arr[x][0] = input("Masukkan Nama Baru         : ")      # Input ulang data Nama baru
            arr[x][1] = int(input("Masukkan No Punggung Baru  : ")) # Input ulang data Nomor punggung baru
            arr[x][2] = int(input("Masukkan Usia Baru         : ")) # Input ulang data Usia baru
            arr[x][3] = input("Masukkan Posisi Baru       : ")      # Input ulang Posisi baru
            arr[x][4] = input("Masukkan Asal Klub Baru    : ")      # Input ulang Asal Klub baru
    if len(found) == 0:                     # Jika array penampung kosong
        print("Kata Kunci Tidak Ditemukan") # Maka tampil "Kata Kunci Tidak Ditemukan"
    print()
        
def hapusData(arr, item):                   # Fungsi Hapus Data
    found = []                              # Array penampung indeks jika tabel ditemukan
    for x in range(0, len(arr)):            # Perulangan sesuai panjang data
        if item == arr[x][0]:               # Jika kata kunci sesuai dengan data
            found.append(x)                 # Maka memasukkan indeks data kedalam array penampung
    arr.pop(found[0])                       # Menghapus data sesuai indeks
    if len(found) == 0:                     # Jika data tidak ada
        print("Kata Kunci Tidak Ditemukan") # Maka tampil "Kata Kunci Tidak Ditemukan"
    else:                                   # Selain itu 
        print("Data Berhasil Dihapus")      # Maka tampil "Data Berhasil Dihapus"
    print()


ulang = True                                # inisiasi variable ulang 
while ulang == True:                        # Program akan terus berjalan dan akan berhenti jika variable ulang = False (user memilih keluar program) 
    print("+==========================================+")
    print("|  PROGRAM DAFTAR PEMAIN TIMNAS INDONESIA  |") # Header Program
    print("+==========================================+")
    print("| Pilihan Menu :                           |") # Menu
    print("| 1. Tambahkan Data Pemain                 |") # Pilihan 1 = tambah data
    print("| 2. Tampilkan Data Pemain                 |") # Pilihan 2 = tampil data
    print("| 3. Sisipkan Data Pemain                  |") # Pilihan 3 = menyisipkan data
    print("| 4. Urutkan Data Pemain                   |") # Pilihan 4 = Sorting data 
    print("| 5. Cari Data Pemain                      |") # Pilihan 5 = Search data
    print("| 6. Ubah Data Pemain                      |") # Pilihan 6 = Mengubah data
    print("| 7. Hapus Data Pemain                     |") # Pilihan 7 = Hapus data
    print("| 8. Keluar Program                        |") # Pilihan 8 = Exit
    print("+------------------------------------------+")
    pil = int(input("Masukkan Pilihan Anda : ")) # Inputan pilihan menu
    print()

    match pil:                                      # Pilihan sesuai inputan pilihan menu oleh user
        case 1:                                     # Pilihan 1 Tambah Data
            print("TAMBAH DATA PEMAIN")
            print()
            tambahkanData(list)                     # Memanggil Fungsi Tambah data
            ulang = True                            # Setelah selesai, maka akan kembali ke pilihan menu utama 
            
        case 2:                                     # Pilihan 2 Tampilkan Data
            print("DAFTAR PEMAIN")
            print()
            tampilkanData(list)                     # Memanggil Fungsi Tampilkan data
            ulang = True                            # Setelah selesai, maka akan kembali ke pilihan menu utama 
            
        case 3:                                     # Pilihan 3 Sisipkan data
            print("SISIPKAN DATA PEMAIN")
            print() 
            baris = int(input("Pemain Akan Disisipkan Pada Baris ke-: "))   # Inputan untuk menentukan data disisipkan pada baris keberapa
            sisipkanData(list, baris)               # Memanggil Fungsi untuk menyisipkan data berdasarkan baris yang di pilih
            ulang = True                            # Setelah selesai, maka akan kembali ke pilihan menu utama 
            
        case 4:                                     # Pilihan 4 Urutkan Data
            print("URUTKAN DAFTAR PEMAIN") 
            print()
            print("Urutkan Berdasarkan :")          # Menu Sorting berdasarkan
            print("1. Nama")                        # Pilihan 1 = nama
            print("2. No Punggung")                 # Pilihan 2 = No Punggung
            print("3. Usia")                        # Pilihan 3 = Usia
            print("4. Posisi")                      # Pilihan 4 = Posisi
            print("5. Asal Klub")                   # Pilihan 5 = Asal klub
            pil = int(input("Masukkan Pilihan Anda : ")) # Input pilihan user agar disortir berdasarkan
            
            match pil:                                      # Pilihan sesuai inputan pilihan menu oleh user
                case 1:                                     # Pilihan 1 sesuai nama
                    print("Urutkan Berdasarkan Nama :")     # Header menu sorting berdasarkan Nama  
                    print("1. Ascending")                   # Pilihan 1 = Ascending
                    print("2. Descending")                  # Pilihan 2 = Descending
                    orderBy = int(input("Masukkan Pilihan Anda : ")) # Input User agar disortir ascending / descending
                    if orderBy == 1:                # Jika memilih 1  
                        shellSort(list, 1, True)    # Maka memanggil fungsi Sorting Asc berdasar nama
                    elif orderBy == 2:              # Jika memilih 2
                        shellSort(list, 1, False)   # Maka memanggil fungsi Sorting Dsc berdasar nama
                        
                case 2:                                     # Pilihan 2 sesuai No Punggung
                    print("Urutkan Berdasarkan No Punggung :") # Header menu sorting berdasarkan No Punggung  
                    print("1. Ascending")                   # Pilihan 1 = Ascending
                    print("2. Descending")                  # Pilihan 2 = Descending
                    orderBy = int(input("Masukkan Pilihan Anda : ")) # Input User agar disortir ascending / descending
                    if orderBy == 1:                # Jika memilih 1
                        shellSort(list, 2, True)    # Maka memanggil fungsi Sorting Asc berdasar no punggung
                    elif orderBy == 2:              # Jika memilih 2
                        shellSort(list, 2, False)   # Maka memanggil fungsi Sorting Dsc berdasar no punggung
                        
                case 3:                                     # Pilihan 3 sesuai usia
                    print("Urutkan Berdasarkan Usia :")     # Header menu sorting berdasarkan Usia
                    print("1. Ascending")                   # Pilihan 1 = Ascending
                    print("2. Descending")                  # Pilihan 2 = Descending
                    orderBy = int(input("Masukkan Pilihan Anda : ")) # Input User agar disortir ascending / descending
                    if orderBy == 1:                # Jika memilih 1
                        shellSort(list, 3, True)    # Maka memanggil fungsi Sorting Asc berdasar usia
                    elif orderBy == 2:              # Jika memilih 2
                        shellSort(list, 3, False)   # Maka memanggil fungsi Sorting Dsc berdasar usia
                        
                case 4:                                     # Pilihan 4 sesuai posisi 
                    print("Urutkan Berdasarkan Posisi :")   # Header menu sorting berdasarkan Usia
                    print("1. Ascending")                   # Pilihan 1 = Ascending
                    print("2. Descending")                  # Pilihan 2 = Descending
                    orderBy = int(input("Masukkan Pilihan Anda : "))  # Input User agar disortir ascending / descending
                    if orderBy == 1:                # Jika memillih 1
                        shellSort(list, 4, True)    # Maka memanggil fungsi Sorting Asc berdasar posisi
                    elif orderBy == 2:              # Jika memilih 2
                        shellSort(list, 4, False)   # Maka memanggil fungsi Sorting Dsc berdasar posisi
                        
                case 5:                                     # Pilihan 5 sesuai asal klub  
                    print("Urutkan Berdasarkan Asal Klub :") # Header menu sorting berdasarkan Asal Klub
                    print("1. Ascending")                   # Pilihan 1 = Ascending
                    print("2. Descending")                  # Pilihan 2 = Descending
                    orderBy = int(input("Masukkan Pilihan Anda : ")) # # Input User agar disortir ascending / descending
                    if orderBy == 1:                # Jika memilih 1
                        shellSort(list, 5, True)    # Maka memanggil fungsi Sorting Asc berdasar asal klub
                    elif orderBy == 2:              # Jika memilih 2
                        shellSort(list, 5, False)   # Maka memanggil fungsi Sorting Dsc berdasar asal klub
                        
            print()
            tampilkanData(list)                     # Memanggil fungsi tampilkan data            
            ulang = True                            # Setelah selesai, maka akan kembali ke pilihan menu utama 
            
        case 5:                                     # Pilihan 5 Pencarian data pemain
            print("PENCARIAN PEMAIN")               
            cari = input("Masukkan Kata Kunci Pencarian : ") # Input user berupa kata kunci pemain
            if any(char.isdigit() for char in cari):         # Jika inputan berupa angka maka menjadi integer
                res = [int(i) for i in cari.split() if i.isdigit()]
                item = int(res[0])
            else:                                            # Jika tidak maka inputan tetap menjadi String 
                item = cari 
            sequentialSearch(list, item)                     # Memanggil fungsi Search
            print()
            ulang = True                                     # Setelah selesai, maka akan kembali ke pilihan menu utama
             
        case 6:                                              # Pilihan 6 ubah data pemain
            print("UBAH DATA PEMAIN")  
            item = input("Masukkan Nama Pemain : ")          # Input user berupa nama pemain yang ingin diubah
            ubahData(list, item)                             # Memanggil Fungsi ubah data  
            ulang = True                                     # Setelah selesai, maka akan kembali ke pilihan menu utama 
            
        case 7:                                              # Pilihan 7 Hapus data
            print("HAPUS DATA PEMAIN")  
            item = input("Masukkan Nama Pemain : ")          # Input user berupa nama pemain yang akan dihapus
            hapusData(list, item)                            # Memanggil fungsi Hapus data 
            ulang = True                                     # Setelah selesai, maka akan kembali ke pilihan menu utama 
            
        case 8:                                              # Pilihan 8 Keluar Program
            konfirmasi = input("Apakah Anda Yakin Keluar Program? (Y/N) : ") # Input user untuk konfirmasi keluar program
            if konfirmasi == "Y" or konfirmasi == "y":       # Jika user menginputkan huruf 'y'
                ulang = False                                # Maka program akan keluar dari perulangan while dan program berhenti
            else:                                            # Jika tidak
                ulang = True                                 # Maka akan kembali ke pilihan menu utama 