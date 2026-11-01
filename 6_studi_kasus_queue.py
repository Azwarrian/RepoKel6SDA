"""
PART 6 : STUDI KASUS QUEUE - ANTREAN PELANGGAN RESTORAN
Pelanggan baru masuk di belakang antrean (enqueue), pelanggan paling
depan dilayani lebih dulu (dequeue) -> sesuai prinsip FIFO.

  - Queue Statis  : tempat tunggu hanya 5 kursi.
  - Queue Dinamis : antrean boleh sepanjang apa pun.

Cara menjalankan:  python 6_studi_kasus_queue.py
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueStatis:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.data = [None] * kapasitas
        self.front = 0
        self.rear = -1
        self.jumlah = 0

    def is_empty(self):
        return self.jumlah == 0

    def is_full(self):
        return self.jumlah == self.kapasitas

    def size(self):
        return self.jumlah

    def enqueue(self, nilai):
        if self.is_full():
            print(f"  [!] Antrean penuh, '{nilai}' tidak bisa masuk")
            return False
        self.rear = (self.rear + 1) % self.kapasitas
        self.data[self.rear] = nilai
        self.jumlah += 1
        return True

    def dequeue(self):
        if self.is_empty():
            print("  [!] Antrean kosong (underflow)")
            return None
        nilai = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.kapasitas
        self.jumlah -= 1
        return nilai

    def peek(self):
        return None if self.is_empty() else self.data[self.front]

    def tampilkan(self):
        isi = [self.data[(self.front + i) % self.kapasitas] for i in range(self.jumlah)]
        print(f"  FRONT -> {isi} <- REAR  (terisi {self.jumlah}/{self.kapasitas})")


class QueueDinamis:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return False

    def size(self):
        return self._size

    def enqueue(self, nilai):
        node = Node(nilai)
        if self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self._size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            print("  [!] Antrean kosong (underflow)")
            return None
        node = self.front
        self.front = node.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return node.data

    def peek(self):
        return None if self.is_empty() else self.front.data

    def tampilkan(self):
        isi, sekarang = [], self.front
        while sekarang:
            isi.append(sekarang.data)
            sekarang = sekarang.next
        print(f"  FRONT -> {isi} <- REAR  (jumlah data {self.size()}, tanpa batas)")


def studi_kasus_restoran(nama, antrean):
    print("\n" + "=" * 70)
    print(f"STUDI KASUS QUEUE - ANTREAN RESTORAN ({nama})")
    print("=" * 70)
    pelanggan_awal = ["Andi", "Budi", "Citra", "Dewi", "Eko", "Fajar", "Gita"]

    print("7 pelanggan datang berurutan:")
    for p in pelanggan_awal:
        if antrean.enqueue(p):
            print(f"  + {p:<6} masuk antrean (panjang antrean: {antrean.size()})")
        else:
            print(f"    -> {p} pulang karena tempat tunggu penuh")

    print("\nAntrean saat ini:")
    antrean.tampilkan()

    print("\nPelayan memanggil 3 pelanggan:")
    for _ in range(3):
        print(f"  Dilayani: {antrean.dequeue()}")

    print("\nPelanggan baru datang (Hana, Indra):")
    for p in ("Hana", "Indra"):
        if antrean.enqueue(p):
            print(f"  + {p} masuk antrean")

    print("\nAntrean saat ini:")
    antrean.tampilkan()

    print("\nSisa pelanggan dilayani sampai antrean kosong:")
    while not antrean.is_empty():
        print(f"  Dilayani: {antrean.dequeue()}")


if __name__ == "__main__":
    studi_kasus_restoran("QUEUE STATIS, 5 kursi tunggu", QueueStatis(5))
    studi_kasus_restoran("QUEUE DINAMIS, tanpa batas", QueueDinamis())

    print("\n" + "=" * 70)
    print("KESIMPULAN")
    print("=" * 70)
    print("  Queue Statis  : jumlah antrean dibatasi, pelanggan berlebih ditolak.")
    print("  Queue Dinamis : semua pelanggan tertampung, memori ikut bertambah.")
