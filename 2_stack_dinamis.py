"""
PART 2 : STACK DINAMIS  (LIFO - Last In, First Out)
Kapasitas fleksibel, memakai Linked List sehingga tidak perlu
menentukan kapasitas maksimum di awal.

Cara menjalankan:  python 2_stack_dinamis.py
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackDinamis:
    def __init__(self):
        self.top = None      # node paling atas
        self._size = 0

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return False         # tidak pernah penuh (selama memori tersedia)

    def size(self):
        return self._size

    def push(self, nilai):
        node = Node(nilai)
        node.next = self.top   # node baru menunjuk ke top lama
        self.top = node        # node baru menjadi top
        self._size += 1
        return True

    def pop(self):
        if self.is_empty():
            print("  [!] Stack kosong (underflow)")
            return None
        node = self.top
        self.top = node.next
        self._size -= 1
        return node.data

    def peek(self):
        return None if self.is_empty() else self.top.data

    def tampilkan(self):
        isi, sekarang = [], self.top
        while sekarang:
            isi.append(sekarang.data)
            sekarang = sekarang.next
        print(f"  TOP -> {isi}  (jumlah data {self.size()}, tanpa batas)")


if __name__ == "__main__":
    print("=" * 60)
    print("PART 2 : STACK DINAMIS (tanpa batas kapasitas)")
    print("=" * 60)

    stack = StackDinamis()

    print("\n1. Push 10, 20, 30")
    for angka in (10, 20, 30):
        stack.push(angka)
    stack.tampilkan()

    print(f"\n2. Peek (lihat data teratas) -> {stack.peek()}")

    print(f"\n3. Pop -> {stack.pop()}   (data terakhir masuk, keluar pertama)")
    stack.tampilkan()

    print("\n4. Push 40, 50, 60, 70 (semua tetap bisa masuk)")
    for angka in (40, 50, 60, 70):
        stack.push(angka)
    stack.tampilkan()

    print("\n5. Pop sampai stack kosong")
    while not stack.is_empty():
        print(f"   pop -> {stack.pop()}")

    print("\n6. Pop saat stack kosong")
    stack.pop()
