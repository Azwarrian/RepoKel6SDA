"""
PART 5 : STUDI KASUS STACK - FITUR UNDO PADA EDITOR TEKS
Setiap aksi pengguna dicatat (push) ke riwayat. Saat UNDO ditekan,
aksi terakhir dikeluarkan (pop) -> sesuai prinsip LIFO.

  - Stack Statis  : riwayat terbatas (misal hanya 5 aksi).
  - Stack Dinamis : riwayat bebas bertambah sesuai kebutuhan.

Cara menjalankan:  python 5_studi_kasus_stack.py
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackStatis:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.data = [None] * kapasitas
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.kapasitas - 1

    def size(self):
        return self.top + 1

    def push(self, nilai):
        if self.is_full():
            print(f"  [!] Stack penuh (overflow), '{nilai}' tidak bisa dimasukkan")
            return False
        self.top += 1
        self.data[self.top] = nilai
        return True

    def pop(self):
        if self.is_empty():
            print("  [!] Stack kosong (underflow)")
            return None
        nilai = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        return nilai

    def peek(self):
        return None if self.is_empty() else self.data[self.top]

    def tampilkan(self):
        isi = [self.data[i] for i in range(self.top, -1, -1)]
        print(f"  TOP -> {isi}  (terisi {self.size()}/{self.kapasitas})")


class StackDinamis:
    def __init__(self):
        self.top = None
        self._size = 0

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return False

    def size(self):
        return self._size

    def push(self, nilai):
        node = Node(nilai)
        node.next = self.top
        self.top = node
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


def studi_kasus_undo(nama, riwayat):
    print("\n" + "=" * 70)
    print(f"STUDI KASUS STACK - UNDO EDITOR TEKS ({nama})")
    print("=" * 70)
    aksi_pengguna = [
        "Ketik 'Halo'", "Ketik ' Dunia'", "Hapus kata 'Dunia'", "Tebalkan teks",
        "Ganti jenis font", "Ubah warna teks", "Sisipkan gambar",
    ]

    print("Pengguna melakukan 7 aksi:")
    for aksi in aksi_pengguna:
        if riwayat.push(aksi):
            print(f"  + {aksi:<22} (riwayat: {riwayat.size()} aksi)")
        else:
            print(f"    -> '{aksi}' tidak tercatat, tidak bisa di-undo!")

    print("\nRiwayat saat ini:")
    riwayat.tampilkan()

    print("\nPengguna menekan UNDO 3 kali:")
    for i in range(1, 4):
        print(f"  Undo ke-{i}: membatalkan '{riwayat.pop()}'")

    print("\nRiwayat tersisa:")
    riwayat.tampilkan()
    print(f"Aksi terakhir yang akan dibatalkan berikutnya: {riwayat.peek()}")


if __name__ == "__main__":
    studi_kasus_undo("STACK STATIS, kapasitas riwayat 5", StackStatis(5))
    studi_kasus_undo("STACK DINAMIS, riwayat tanpa batas", StackDinamis())

    print("\n" + "=" * 70)
    print("KESIMPULAN")
    print("=" * 70)
    print("  Stack Statis  : hemat & mudah diprediksi, tetapi riwayat undo terbatas.")
    print("  Stack Dinamis : riwayat undo fleksibel, tetapi memori ikut bertambah.")
