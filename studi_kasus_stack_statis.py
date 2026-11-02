"""
Studi Kasus Stack (STATIS / ARRAY)
  1. Pengecekan kurung seimbang
  2. Membalik kata & cek palindrom
"""
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE, "..", "..", "Library Stack", "Statis"))

from stack_statis import StackStatis  # noqa: E402


# ---------- Kasus 1: Kurung seimbang ----------
def kurung_seimbang(ekspresi):
    pasangan = {")": "(", "]": "[", "}": "{"}
    stack = StackStatis(max(1, len(ekspresi)))  # kapasitas cukup untuk kasus terburuk
    for i, ch in enumerate(ekspresi, start=1):
        if ch in "([{":
            stack.push(ch)
        elif ch in ")]}":
            if stack.is_empty():
                return False, f"Kurung '{ch}' di posisi {i} tidak punya pasangan pembuka."
            buka = stack.pop()
            if buka != pasangan[ch]:
                return False, f"Kurung '{ch}' di posisi {i} tidak cocok dengan '{buka}'."
    if not stack.is_empty():
        return False, f"Ada {stack.size()} kurung pembuka yang belum ditutup."
    return True, "Kurung seimbang."


def kasus_kurung():
    print("\n--- Pengecekan Kurung Seimbang ---")
    print("Contoh: {[()]} seimbang, ([)] tidak seimbang")
    ekspresi = input("Masukkan ekspresi: ")
    ok, pesan = kurung_seimbang(ekspresi)
    print(("  [OK] " if ok else "  [X]  ") + pesan)


# ---------- Kasus 2: Balik kata & palindrom ----------
def balik_teks(teks):
    stack = StackStatis(max(1, len(teks)))
    for ch in teks:
        stack.push(ch)
    hasil = ""
    while not stack.is_empty():
        hasil += stack.pop()
    return hasil


def kasus_palindrom():
    print("\n--- Balik Kata & Cek Palindrom ---")
    teks = input("Masukkan kata/kalimat: ")
    print(f"  Hasil dibalik : {balik_teks(teks)}")
    bersih = "".join(c.lower() for c in teks if c.isalnum())
    if bersih and bersih == balik_teks(bersih):
        print("  Palindrom     : YA")
    else:
        print("  Palindrom     : TIDAK")


def main():
    while True:
        print("\n=== STUDI KASUS STACK (STATIS) ===")
        print("1. Pengecekan kurung seimbang")
        print("2. Balik kata & cek palindrom")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            kasus_kurung()
        elif pilihan == "2":
            kasus_palindrom()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("  Pilihan tidak valid.")


if __name__ == "__main__":
    main()
