"""
PART 1 : STACK STATIS  (LIFO - Last In, First Out)
Kapasitas tetap sejak awal (berbasis list/array berukuran tetap).

Cara menjalankan:  python 1_stack_statis.py
"""


class StackStatis:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.data = [None] * kapasitas   # memori dialokasikan tetap di awal
        self.top = -1                    # -1 artinya stack kosong

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.kapasitas - 1

    def size(self):
        return self.top + 1

    def push(self, nilai):
        """Memasukkan data ke puncak stack. Gagal jika stack penuh."""
        if self.is_full():
            print(f"  [!] Stack penuh (overflow), '{nilai}' tidak bisa dimasukkan")
            return False
        self.top += 1
        self.data[self.top] = nilai
        return True

    def pop(self):
        """Mengeluarkan data teratas. Mengembalikan None jika stack kosong."""
        if self.is_empty():
            print("  [!] Stack kosong (underflow)")
            return None
        nilai = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        return nilai

    def peek(self):
        """Melihat data teratas tanpa mengeluarkannya."""
        return None if self.is_empty() else self.data[self.top]

    def tampilkan(self):
        isi = [self.data[i] for i in range(self.top, -1, -1)]
        print(f"  TOP -> {isi}  (terisi {self.size()}/{self.kapasitas})")


if __name__ == "__main__":
    print("=" * 60)
    print("PART 1 : STACK STATIS (kapasitas 5)")
    print("=" * 60)

    stack = StackStatis(5)

    print("\n1. Push 10, 20, 30")
    for angka in (10, 20, 30):
        stack.push(angka)
    stack.tampilkan()

    print(f"\n2. Peek (lihat data teratas) -> {stack.peek()}")

    print(f"\n3. Pop -> {stack.pop()}   (data terakhir masuk, keluar pertama)")
    stack.tampilkan()

    print("\n4. Push 40, 50, 60, 70 (kapasitas hanya 5)")
    for angka in (40, 50, 60, 70):
        stack.push(angka)
    stack.tampilkan()

    print("\n5. Pop sampai stack kosong")
    while not stack.is_empty():
        print(f"   pop -> {stack.pop()}")

    print("\n6. Pop saat stack kosong")
    stack.pop()
