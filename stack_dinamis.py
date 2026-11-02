class Node:
    __slots__ = ("data", "next")

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class StackDinamis:
    """Stack dinamis: linked list, ukuran tumbuh sesuai kebutuhan (tanpa batas tetap)."""

    def __init__(self):
        self.top = None
        self._size = 0

    def is_empty(self):
        return self.top is None

    def is_full(self):
        # Dinamis tidak pernah penuh (selama memori tersedia).
        return False

    def size(self):
        return self._size

    def push(self, item):
        self.top = Node(item, self.top)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack kosong (underflow)")
        item = self.top.data
        self.top = self.top.next
        self._size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack kosong")
        return self.top.data

    def clear(self):
        self.top = None
        self._size = 0

    def to_list(self):
        """Isi stack dari dasar ke puncak."""
        hasil = []
        cur = self.top
        while cur:
            hasil.append(cur.data)
            cur = cur.next
        hasil.reverse()
        return hasil

    def display(self):
        if self.is_empty():
            print("  (stack kosong)")
            return
        cur = self.top
        while cur:
            tanda = "  <- TOP" if cur is self.top else ""
            print(f"  [ {cur.data} ]{tanda}")
            if cur.next:
                print("     |")
            cur = cur.next

    def __len__(self):
        return self._size

    def __str__(self):
        return "Stack" + str(self.to_list())


if __name__ == "__main__":
    s = StackDinamis()
    for x in (1, 2, 3):
        s.push(x)
    s.display()
    print("Pop:", s.pop(), "| Peek:", s.peek(), "| Size:", s.size())
