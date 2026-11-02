"""
Studi Kasus Queue (STATIS / CIRCULAR ARRAY)
  1. Antrian loket bank (ruang tunggu terbatas)
  2. Hot Potato / Josephus (permainan eliminasi)
"""
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE, "..", "..", "Library Queue", "Statis"))

from queue_statis import QueueStatis  # noqa: E402


def input_int(prompt, minimum=None):
    while True:
        try:
            nilai = int(input(prompt))
        except ValueError:
            print("  Input harus berupa angka bulat.")
            continue
        if minimum is not None and nilai < minimum:
            print(f"  Nilai minimal {minimum}.")
            continue
        return nilai


# ---------- Kasus 1: Antrian bank ----------
class LoketBank:
    def __init__(self, kapasitas):
        self.antrian = QueueStatis(kapasitas)
        self.nomor_terakhir = 0

    def ambil_nomor(self, nama):
        if self.antrian.is_full():
            raise OverflowError("Ruang tunggu penuh, silakan menunggu sebentar.")
        self.nomor_terakhir += 1
        entri = f"A{self.nomor_terakhir:03d} {nama}"
        self.antrian.enqueue(entri)
        return entri

    def panggil(self):
        return self.antrian.dequeue()


def kasus_bank():
    kapasitas = input_int("Kapasitas ruang tunggu bank: ", 1)
    loket = LoketBank(kapasitas)
    while True:
        print("\n--- ANTRIAN LOKET BANK ---")
        print("1. Ambil nomor antrian")
        print("2. Panggil nasabah berikutnya")
        print("3. Lihat antrian")
        print("4. Siapa berikutnya?")
        print("0. Kembali")
        pilihan = input("Pilih: ").strip()
        try:
            if pilihan == "1":
                nama = input("Nama nasabah: ").strip() or "Tanpa nama"
                print(f"  Nomor antrian Anda: {loket.ambil_nomor(nama)}")
            elif pilihan == "2":
                print(f"  Memanggil: {loket.panggil()} -> silakan ke loket.")
            elif pilihan == "3":
                loket.antrian.display()
                print(f"  Menunggu: {loket.antrian.size()} / {kapasitas}")
            elif pilihan == "4":
                print(f"  Berikutnya: {loket.antrian.peek_front()}")
            elif pilihan == "0":
                break
            else:
                print("  Pilihan tidak valid.")
        except (OverflowError, IndexError) as e:
            print(f"  {e}")


# ---------- Kasus 2: Hot Potato ----------
def hot_potato(daftar_nama, k):
    antrian = QueueStatis(len(daftar_nama))
    for nama in daftar_nama:
        antrian.enqueue(nama)
    urutan_keluar = []
    while antrian.size() > 1:
        for _ in range(k - 1):
            antrian.enqueue(antrian.dequeue())  # oper bola ke belakang antrian
        urutan_keluar.append(antrian.dequeue())  # yang memegang bola tereliminasi
    return urutan_keluar, antrian.dequeue()


def kasus_hot_potato():
    print("\n--- HOT POTATO (JOSEPHUS) ---")
    daftar = [n.strip() for n in input("Nama pemain (pisahkan koma): ").split(",") if n.strip()]
    if len(daftar) < 2:
        print("  Minimal 2 pemain.")
        return
    k = input_int("Hitungan oper bola (k): ", 1)
    keluar, pemenang = hot_potato(daftar, k)
    for i, nama in enumerate(keluar, start=1):
        print(f"  Putaran {i}: {nama} tereliminasi")
    print(f"  Pemenang: {pemenang}")


def main():
    while True:
        print("\n=== STUDI KASUS QUEUE (STATIS) ===")
        print("1. Antrian loket bank")
        print("2. Hot Potato (Josephus)")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            kasus_bank()
        elif pilihan == "2":
            kasus_hot_potato()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("  Pilihan tidak valid.")


if __name__ == "__main__":
    main()
