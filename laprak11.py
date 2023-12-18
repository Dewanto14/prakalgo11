# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 14:00:34 2023

@author: Huawei
"""

class Mahasiswa:
    jumlah = 0
    
    def __init__(self, nama, nilai):
        self.__nama = nama  
        self.__nilai = nilai
        Mahasiswa.jumlah +=1
        
    def dislayCount(self):
        print("Total Mahasiswa %d" %Mahasiswa.jumlah)
        
    def displayMahasiswa(self):
        print("Nama:", self.__nama if self.__nama is not None else "None", "\nNilai:", self.__nilai if self.__nilai is not None else "None")

        
    def ubahData(self, nama_baru=None, nilai_baru=None):
        if nama_baru is not None:
            self.__nama = nama_baru
        if nilai_baru is not None:
            self.__nilai = nilai_baru
        print("Data mahasiswa berhasil diubah")
        
    def displayubah(self):
        print("Nama: ",None, "\nNilai : ")
        
    def getNama(self):
        return self.__nama
    
    def setName(self, nama_baru):
        self.__nama = nama_baru
        
    def getNilai(self):
        return self.__nilai
    
    def setNilai(self, nilai_baru):
        self.__nilai = nilai_baru
        
def tampilkan_menu():
    print("=== Program OOP ===")
    print("1. Mendeklarasikan Objek")
    print("2. Menampilkan Jumlah Objek")
    print("3. Menampilkan Objek")
    print("4. Merubah Nilai Objek")
    print("5. Menghapus Objek")
    print("6. Keluar Dari Program")


def hapus_mahasiswa(nama_mahasiswa, daftar_mahasiswa):
    for mahasiswa in daftar_mahasiswa:
        if mahasiswa.getNama() == nama_mahasiswa:
            daftar_mahasiswa.remove(mahasiswa)
            print("Mahasiswa berhasil dihapus!")
            return
    else:
        print("Mahasiswa tidak ditemukan.")



daftar_mahasiswa = []

while True:
    tampilkan_menu()
    print()
    pilihan = input("Masukkan Pilihan Berupa Angka (1/2/3/4/5/6): ")

    if pilihan == '1':
        nama_mahasiswa = input("Masukkan nama mahasiswa: ")
        nilai_mahasiswa = int(input("Masukkan nilai mahasiswa: "))
        mahasiswa_baru = Mahasiswa(nama_mahasiswa, nilai_mahasiswa)
        daftar_mahasiswa.append(mahasiswa_baru)
        print("Mahasiswa berhasil ditambahkan!")
        print()

    elif pilihan == '2':
        print("Total Mahasiswa %d" % Mahasiswa.jumlah)
        print()
        
    elif pilihan == '3':
        print()
        for mahasiswa in daftar_mahasiswa:
                mahasiswa.displayMahasiswa()

                print()


    elif pilihan == '4':
        nama_cari = input("Masukkan nama mahasiswa yang ingin diubah: ")
        for mahasiswa in daftar_mahasiswa:
            if mahasiswa.getNama() == nama_cari:
                print("1. Ubah Nama")
                print("2. Ubah Nilai")
                pilihan_ubah = input("Pilih yang ingin diubah (1/2): ")

                if pilihan_ubah == '1':
                    nama_baru = input("Masukkan nama baru: ")
                    mahasiswa.ubahData(nama_baru=nama_baru)
                    print()
                elif pilihan_ubah == '2':
                    nilai_baru = int(input("Masukkan nilai baru: "))
                    mahasiswa.ubahData(nilai_baru=nilai_baru)
                    print()
                else:
                    print("Pilihan tidak valid.")
                break
        else:
            print("Mahasiswa tidak ditemukan.")
            print()
    elif pilihan == '5':
        nama_hapus = input("Masukkan nama mahasiswa yang ingin dihapus: ")
        hapus_mahasiswa(nama_hapus, daftar_mahasiswa)
        mahasiswa.Nama = None
        mahasiswa.Nilai = None
        mhs_baru = Mahasiswa(mahasiswa.Nama, mahasiswa.Nilai)
        daftar_mahasiswa.append(mhs_baru)
        print()
        
    elif pilihan == '6':
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih antara 1-6.")