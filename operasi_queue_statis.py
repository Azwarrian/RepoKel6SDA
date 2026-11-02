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


def tampil_menu():
    print("\n=== OPERASI QUEUE (STATIS / CIRCULAR ARRAY) ===")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek depan (front)")
    print("4. Peek belakang (rear)")
    print("5. Tampilkan queue")
    print("6. Cek kosong / penuh")
    print("7. Jumlah elemen")
    print("8. Kosongkan queue")
    print("0. Keluar")


def main():
    kapasitas = input_int("Masukkan kapasitas queue: ", 1)
    queue = QueueStatis(kapasitas)

    while True:
        tampil_menu()
        pilihan = input("Pilih menu: ").strip()
        try:
            if pilihan == "1":
                item = input("Masukkan data: ")
                queue.enqueue(item)
                print(f"  '{item}' berhasil di-enqueue.")
            elif pilihan == "2":
                print(f"  Data di-dequeue: {queue.dequeue()}")
            elif pilihan == "3":
                print(f"  Elemen depan: {queue.peek_front()}")
            elif pilihan == "4":
                print(f"  Elemen belakang: {queue.peek_rear()}")
            elif pilihan == "5":
                queue.display()
            elif pilihan == "6":
                print(f"  Kosong: {queue.is_empty()} | Penuh: {queue.is_full()}")
            elif pilihan == "7":
                print(f"  Jumlah elemen: {queue.size()} dari {queue.kapasitas}")
            elif pilihan == "8":
                queue.clear()
                print("  Queue dikosongkan.")
            elif pilihan == "0":
                print("Program selesai.")
                break
            else:
                print("  Pilihan tidak valid.")
        except (OverflowError, IndexError) as e:
            print(f"  Error: {e}")


if __name__ == "__main__":
    main()
