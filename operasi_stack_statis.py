import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE, "..", "..", "Library Stack", "Statis"))

from stack_statis import StackStatis  # noqa: E402


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
    print("\n=== OPERASI STACK (STATIS / ARRAY) ===")
    print("1. Push")
    print("2. Pop")
    print("3. Peek (lihat elemen teratas)")
    print("4. Tampilkan stack")
    print("5. Cek kosong / penuh")
    print("6. Jumlah elemen")
    print("7. Kosongkan stack")
    print("0. Keluar")


def main():
    kapasitas = input_int("Masukkan kapasitas stack: ", 1)
    stack = StackStatis(kapasitas)

    while True:
        tampil_menu()
        pilihan = input("Pilih menu: ").strip()
        try:
            if pilihan == "1":
                item = input("Masukkan data: ")
                stack.push(item)
                print(f"  '{item}' berhasil di-push.")
            elif pilihan == "2":
                print(f"  Data di-pop: {stack.pop()}")
            elif pilihan == "3":
                print(f"  Elemen teratas: {stack.peek()}")
            elif pilihan == "4":
                stack.display()
            elif pilihan == "5":
                print(f"  Kosong: {stack.is_empty()} | Penuh: {stack.is_full()}")
            elif pilihan == "6":
                print(f"  Jumlah elemen: {stack.size()} dari {stack.kapasitas}")
            elif pilihan == "7":
                stack.clear()
                print("  Stack dikosongkan.")
            elif pilihan == "0":
                print("Program selesai.")
                break
            else:
                print("  Pilihan tidak valid.")
        except (OverflowError, IndexError) as e:
            print(f"  Error: {e}")


if __name__ == "__main__":
    main()
