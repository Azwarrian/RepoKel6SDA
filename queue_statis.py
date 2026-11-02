class QueueStatis:
    """Queue statis: circular array berukuran tetap (FIFO)."""

    def __init__(self, kapasitas=10):
        if kapasitas <= 0:
            raise ValueError("Kapasitas harus lebih dari 0")
        self.kapasitas = kapasitas
        self.data = [None] * kapasitas
        self.front = 0
        self.rear = -1
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self.kapasitas

    def size(self):
        return self._size

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue penuh (overflow)")
        self.rear = (self.rear + 1) % self.kapasitas
        self.data[self.rear] = item
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue kosong (underflow)")
        item = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.kapasitas
        self._size -= 1
        return item

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue kosong")
        return self.data[self.front]

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("Queue kosong")
        return self.data[self.rear]

    def clear(self):
        self.data = [None] * self.kapasitas
        self.front = 0
        self.rear = -1
        self._size = 0

    def to_list(self):
        """Isi queue dari depan ke belakang."""
        return [self.data[(self.front + i) % self.kapasitas] for i in range(self._size)]

    def display(self):
        if self.is_empty():
            print("  (queue kosong)")
            return
        isi = " ".join(f"[{x}]" for x in self.to_list())
        print(f"  DEPAN -> {isi} <- BELAKANG")

    def __len__(self):
        return self._size

    def __str__(self):
        return "Queue" + str(self.to_list())


if __name__ == "__main__":
    q = QueueStatis(3)
    for x in ("A", "B", "C"):
        q.enqueue(x)
    q.display()
    print("Dequeue:", q.dequeue(), "| Front:", q.peek_front(), "| Rear:", q.peek_rear())
    q.enqueue("D")  # menguji circular
    q.display()
