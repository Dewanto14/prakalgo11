# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 13:09:09 2023

@author: Huawei
"""

class Mahasiswa:
    jumlah = 0
    
    def __init__(self, name, nim, angkatan):
        self.name = name
        self.nim = nim
        self.angkatan = angkatan
        Mahasiswa.jumlah +=1
        
    def displayCount(self):
        print("Total Mahasiswa %d" %Mahasiswa.jumlah)
        
    def displayMahasiswa(self):
        print("Name: ",self.name, "\nNIM: ",self.nim, "\nAngkatan: ",self.angkatan)
        
nama = input("Masukkan Namamu: ")
nim = input("Masukkan NIM kamu: ")
angkatan = input("Masukkan Angkatan: ")

print("\n")
mhs1 = Mahasiswa(nama, nim, angkatan)
mhs1.displayMahasiswa()
print("\n")
print("Total Mahasiswa %d" % Mahasiswa.jumlah)