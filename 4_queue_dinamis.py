"""
PART 4 : QUEUE DINAMIS  (FIFO - First In, First Out)
Kapasitas fleksibel, memakai Linked List sehingga tidak ada
kapasitas maksimum yang ditentukan di awal.

Cara menjalankan:  python 4_queue_dinamis.py
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueDinamis:
    def __init__(self):
        self.front = None    # node terdepan (keluar)
        self.rear = None     # node paling belakang (masuk)
        self._size = 0

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return False

    def size(self):
        return self._size

    def enqueue(self, nilai):
        node = Node(nilai)
        if self.rear is None:          # antrean masih kosong
            self.front = self.rear = node
        else:
            self.rear.next = node      # sambungkan di belakang
            self.rear = node
        self._size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            print("  [!] Antrean kosong (underflow)")
            return None
        node = self.front
        self.front = node.next
        if self.front is None:         # antrean menjadi kosong
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


if __name__ == "__main__":
    print("=" * 60)
    print("PART 4 : QUEUE DINAMIS (tanpa batas kapasitas)")
    print("=" * 60)

    queue = QueueDinamis()

    print("\n1. Enqueue 10, 20, 30")
    for angka in (10, 20, 30):
        queue.enqueue(angka)
    queue.tampilkan()

    print(f"\n2. Peek (lihat data terdepan) -> {queue.peek()}")

    print(f"\n3. Dequeue -> {queue.dequeue()}   (data pertama masuk, keluar pertama)")
    queue.tampilkan()

    print("\n4. Enqueue 40, 50, 60, 70 (semua tetap bisa masuk)")
    for angka in (40, 50, 60, 70):
        queue.enqueue(angka)
    queue.tampilkan()

    print("\n5. Dequeue sampai antrean kosong")
    while not queue.is_empty():
        print(f"   dequeue -> {queue.dequeue()}")

    print("\n6. Dequeue saat antrean kosong")
    queue.dequeue()
