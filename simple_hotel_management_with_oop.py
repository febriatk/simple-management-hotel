# -*- coding: utf-8 -*-
"""Simple Hotel Management with OOP

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ydSmw_VPwfENNPoNaTvjGQ-D6xj4K85n
"""

import pickle
import os


class Hotel:
    def __init__(self, room_no=0, date_in="", date_out="", name="", mob="", address=""):
        self.room_no = room_no
        self.date_in = date_in
        self.date_out = date_out
        self.name = name
        self.mob = mob
        self.address = address

    def accept(self):
        self.date_in = input("\nTanggal check-in: ")
        self.name = input("\nNama lengkap: ")
        self.mob = input("\nNomor telepon: ")
        self.address = input("\nAlamat: ")

    def display(self):
        print(f"\nNomor Kamar   : {self.room_no}")
        print(f"\nNama          : {self.name}")
        print(f"\nNomor Telepon : {self.mob}")
        print(f"\nAlamat        : {self.address}")
        print("----------------------------")


class HotelManagement:
    FILE = "rekam.pkl"
    BACKUP = "back.pkl"

    def __init__(self):
        self.rooms = self.load_records(HotelManagement.FILE)
        self.backup = self.load_records(HotelManagement.BACKUP)
        self.room_list = [101, 102, 103, 104, 105, 201, 202, 203, 204, 205, 301, 302, 303, 304, 305]

    @staticmethod
    def load_records(filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                return pickle.load(file)
        return []

    @staticmethod
    def save_records(filename, data):
        with open(filename, 'wb') as file:
            pickle.dump(data, file)

    def check(self, room_no):
        return room_no in self.room_list and all(room.room_no != room_no for room in self.rooms)

    def allot_room(self):
        room_no = int(input("\nMasukkan nomor kamar: "))
        if not self.check(room_no):
            print("\nKamar tidak tersedia atau sudah dipesan.")
        else:
            room = Hotel(room_no=room_no)
            room.accept()
            self.rooms.append(room)
            self.room_list.remove(room_no)
            self.save_records(HotelManagement.FILE, self.rooms)
            print("\nKamar berhasil dipesan.")

    def available_room_status(self):
        if self.room_list :
            print("\nKamar tersedia:")
            for room_no in self.room_list:
                print(f"- Kamar {room_no} ")
        else:
            print("\nTidak ada kamar yang tersedia.")

    def edit(self):
        room_no = int(input("\nMasukkan nomor kamar lama: "))
        for room in self.rooms:
            if room.room_no == room_no:
                room.room_no = int(input("\nMasukkan nomor kamar baru: "))
                room.accept()
                self.save_records(HotelManagement.FILE, self.rooms)
                print("\nData berhasil diperbarui.")
                return
        print("\nNomor kamar tidak ditemukan.")

    def room_info(self):
        room_no = int(input("\nMasukkan nomor kamar: "))
        for room in self.rooms:
            if room.room_no == room_no:
                room.display()
                return
        print("\nKamar tersebut kosong.")

    def customer_info(self):
        name = input("\nMasukkan nama : ").lower()
        found = False
        for room in self.rooms:
            if name in room.name.lower():
                room.display()
                found = True
        if not found:
            print("\nDetail pelanggan tidak ditemukan.")

    def leave_room(self):
        room_no = int(input("\nNomor kamar: "))
        for room in self.rooms:
            if room.room_no == room_no:
                room.date_out = input("\nTanggal check-out: ")
                self.backup.append(room)
                self.rooms.remove(room)
                self.room_list.append(room_no)
                self.save_records(HotelManagement.FILE, self.rooms)
                self.save_records(HotelManagement.BACKUP, self.backup)
                print("\nCheck-out berhasil.")
                return
        print("\nNomor kamar tidak ditemukan.")

    def old_records(self):
        if self.backup:
            print("\nRiwayat Pemesanan:")
            for room in self.backup:
                room.display()
                print(f"\nTanggal Check-Out: {room.date_out}")
        else:
            print("\nTidak ada riwayat pemesanan.")


def main():
    hotel_management = HotelManagement()

    while True:
        print("\nSELAMAT DATANG DI HOTEL PANGLIMA")
        print("________________________________")
        print("1. Pesan Kamar")
        print("2. Melihat Status Kamar")
        print("3. Melihat Informasi Kamar")
        print("4. Melihat Informasi Pelanggan")
        print("5. Edit Data")
        print("6. Check-Out Kamar")
        print("7. Melihat Riwayat Pemesanan")
        print("0. Keluar")
        print("________________________________")
        choice = int(input("\nMasukkan Pilihan Anda: "))

        if choice == 1:
            hotel_management.allot_room()
        elif choice == 2:
            hotel_management.available_room_status()
        elif choice == 3:
            hotel_management.room_info()
        elif choice == 4:
            hotel_management.customer_info()
        elif choice == 5:
            hotel_management.edit()
        elif choice == 6:
            hotel_management.leave_room()
        elif choice == 7:
            hotel_management.old_records()
        elif choice == 0:
            print("\nSELAMAT TINGGAL!")
            break
        else:
            print("\nPilihan tidak valid, coba lagi.")


if __name__ == "__main__":
    main()
