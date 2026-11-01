"""
PART 3 : QUEUE STATIS  (FIFO - First In, First Out)
Kapasitas tetap sejak awal. Memakai array melingkar (circular) agar
tempat yang kosong setelah dequeue bisa dipakai lagi oleh data baru.

Cara menjalankan:  python 3_queue_statis.py
"""


class QueueStatis:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.data = [None] * kapasitas
        self.front = 0       # indeks data paling depan (keluar)
        self.rear = -1       # indeks data paling belakang (masuk)
        self.jumlah = 0

    def is_empty(self):
        return self.jumlah == 0

    def is_full(self):
        return self.jumlah == self.kapasitas

    def size(self):
        return self.jumlah

    def enqueue(self, nilai):
        """Memasukkan data di belakang antrean. Gagal jika antrean penuh."""
        if self.is_full():
            print(f"  [!] Antrean penuh, '{nilai}' tidak bisa masuk")
            return False
        self.rear = (self.rear + 1) % self.kapasitas
        self.data[self.rear] = nilai
        self.jumlah += 1
        return True

    def dequeue(self):
        """Mengeluarkan data terdepan. Mengembalikan None jika kosong."""
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


if __name__ == "__main__":
    print("=" * 60)
    print("PART 3 : QUEUE STATIS (kapasitas 5)")
    print("=" * 60)

    queue = QueueStatis(5)

    print("\n1. Enqueue 10, 20, 30")
    for angka in (10, 20, 30):
        queue.enqueue(angka)
    queue.tampilkan()

    print(f"\n2. Peek (lihat data terdepan) -> {queue.peek()}")

    print(f"\n3. Dequeue -> {queue.dequeue()}   (data pertama masuk, keluar pertama)")
    queue.tampilkan()

    print("\n4. Enqueue 40, 50, 60, 70 (kapasitas hanya 5)")
    for angka in (40, 50, 60, 70):
        queue.enqueue(angka)
    queue.tampilkan()

    print("\n5. Dequeue 2 kali, lalu Enqueue 70 dan 80 (tempat kosong dipakai lagi)")
    print(f"   dequeue -> {queue.dequeue()}")
    print(f"   dequeue -> {queue.dequeue()}")
    queue.enqueue(70)
    queue.enqueue(80)
    queue.tampilkan()

    print("\n6. Dequeue sampai antrean kosong")
    while not queue.is_empty():
        print(f"   dequeue -> {queue.dequeue()}")

    print("\n7. Dequeue saat antrean kosong")
    queue.dequeue()
