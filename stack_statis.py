class StackStatis:
    """Stack statis: array (list) berukuran tetap, kapasitas ditentukan di awal."""

    def __init__(self, kapasitas=10):
        if kapasitas <= 0:
            raise ValueError("Kapasitas harus lebih dari 0")
        self.kapasitas = kapasitas
        self.data = [None] * kapasitas
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.kapasitas - 1

    def size(self):
        return self.top + 1

    def push(self, item):
        if self.is_full():
            raise OverflowError("Stack penuh (overflow)")
        self.top += 1
        self.data[self.top] = item

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack kosong (underflow)")
        item = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack kosong")
        return self.data[self.top]

    def clear(self):
        self.data = [None] * self.kapasitas
        self.top = -1

    def to_list(self):
        """Isi stack dari dasar ke puncak."""
        return self.data[: self.top + 1]

    def display(self):
        if self.is_empty():
            print("  (stack kosong)")
            return
        print("  +------------+")
        for i in range(self.top, -1, -1):
            tanda = "  <- TOP" if i == self.top else ""
            print(f"  | {str(self.data[i]):^10} |{tanda}")
            print("  +------------+")

    def __len__(self):
        return self.size()

    def __str__(self):
        return "Stack" + str(self.to_list())


if __name__ == "__main__":
    s = StackStatis(3)
    for x in (1, 2, 3):
        s.push(x)
    s.display()
    print("Pop:", s.pop(), "| Peek:", s.peek(), "| Size:", s.size())
