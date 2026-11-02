class Node:
    __slots__ = ("data", "next")

    def __init__(self, data):
        self.data = data
        self.next = None


class QueueDinamis:
    """Queue dinamis: linked list dengan pointer head (depan) dan tail (belakang)."""

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self.head is None

    def is_full(self):
        # Dinamis tidak pernah penuh (selama memori tersedia).
        return False

    def size(self):
        return self._size

    def enqueue(self, item):
        node = Node(item)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue kosong (underflow)")
        item = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return item

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue kosong")
        return self.head.data

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("Queue kosong")
        return self.tail.data

    def clear(self):
        self.head = self.tail = None
        self._size = 0

    def to_list(self):
        """Isi queue dari depan ke belakang."""
        hasil = []
        cur = self.head
        while cur:
            hasil.append(cur.data)
            cur = cur.next
        return hasil

    def display(self):
        if self.is_empty():
            print("  (queue kosong)")
            return
        isi = " -> ".join(f"[{x}]" for x in self.to_list())
        print(f"  DEPAN: {isi} :BELAKANG")

    def __len__(self):
        return self._size

    def __str__(self):
        return "Queue" + str(self.to_list())


if __name__ == "__main__":
    q = QueueDinamis()
    for x in ("A", "B", "C"):
        q.enqueue(x)
    q.display()
    print("Dequeue:", q.dequeue(), "| Front:", q.peek_front(), "| Rear:", q.peek_rear())
