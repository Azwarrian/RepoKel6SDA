"""
Studi Kasus Stack (DINAMIS / LINKED LIST)
  1. Konversi infix -> postfix + evaluasi
  2. Undo / Redo editor teks
"""
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE, "..", "..", "Library Stack", "Dinamis"))

from stack_dinamis import StackDinamis  # noqa: E402


# ---------- Kasus 1: Infix -> Postfix + Evaluasi ----------
PRESEDENSI = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}


def tokenisasi(ekspresi):
    token = []
    i = 0
    while i < len(ekspresi):
        c = ekspresi[i]
        if c.isspace():
            i += 1
        elif c.isdigit() or c == ".":
            j = i
            while j < len(ekspresi) and (ekspresi[j].isdigit() or ekspresi[j] == "."):
                j += 1
            token.append(ekspresi[i:j])
            i = j
        elif c in PRESEDENSI or c in "()":
            token.append(c)
            i += 1
        else:
            raise ValueError(f"Karakter tidak dikenal: '{c}'")
    return token


def infix_ke_postfix(token):
    output = []
    stack = StackDinamis()
    for t in token:
        if t == "(":
            stack.push(t)
        elif t == ")":
            while not stack.is_empty() and stack.peek() != "(":
                output.append(stack.pop())
            if stack.is_empty():
                raise ValueError("Kurung tutup tanpa pasangan.")
            stack.pop()  # buang '('
        elif t in PRESEDENSI:
            while (
                not stack.is_empty()
                and stack.peek() != "("
                and (
                    PRESEDENSI[stack.peek()] > PRESEDENSI[t]
                    or (PRESEDENSI[stack.peek()] == PRESEDENSI[t] and t != "^")
                )
            ):
                output.append(stack.pop())
            stack.push(t)
        else:
            output.append(t)  # operand
    while not stack.is_empty():
        op = stack.pop()
        if op == "(":
            raise ValueError("Kurung buka tanpa penutup.")
        output.append(op)
    return output


def evaluasi_postfix(postfix):
    stack = StackDinamis()
    for t in postfix:
        if t in PRESEDENSI:
            if stack.size() < 2:
                raise ValueError("Ekspresi tidak valid.")
            b = stack.pop()
            a = stack.pop()
            if t == "+":
                stack.push(a + b)
            elif t == "-":
                stack.push(a - b)
            elif t == "*":
                stack.push(a * b)
            elif t == "/":
                if b == 0:
                    raise ZeroDivisionError("Pembagian dengan nol.")
                stack.push(a / b)
            elif t == "^":
                stack.push(a ** b)
        else:
            try:
                stack.push(float(t))
            except ValueError:
                raise ValueError(f"Angka tidak valid: '{t}'")
    if stack.size() != 1:
        raise ValueError("Ekspresi tidak valid.")
    return stack.pop()


def format_angka(x):
    return str(int(x)) if x == int(x) else f"{x:.4f}".rstrip("0")


def kasus_postfix():
    print("\n--- Infix -> Postfix + Evaluasi ---")
    print("Operator: + - * / ^ dan kurung ( ). Contoh: (3 + 4) * 2 ^ 2 - 5")
    ekspresi = input("Masukkan ekspresi infix: ")
    try:
        postfix = infix_ke_postfix(tokenisasi(ekspresi))
        print(f"  Postfix : {' '.join(postfix)}")
        print(f"  Hasil   : {format_angka(evaluasi_postfix(postfix))}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"  Error: {e}")


# ---------- Kasus 2: Undo / Redo ----------
class EditorTeks:
    def __init__(self):
        self.teks = ""
        self.undo_stack = StackDinamis()
        self.redo_stack = StackDinamis()

    def _ubah(self, teks_baru):
        self.undo_stack.push(self.teks)
        self.redo_stack.clear()  # aksi baru menghapus riwayat redo
        self.teks = teks_baru

    def tulis(self, tambahan):
        self._ubah(self.teks + tambahan)

    def hapus(self, n):
        self._ubah(self.teks[: max(0, len(self.teks) - n)])

    def undo(self):
        if self.undo_stack.is_empty():
            return False
        self.redo_stack.push(self.teks)
        self.teks = self.undo_stack.pop()
        return True

    def redo(self):
        if self.redo_stack.is_empty():
            return False
        self.undo_stack.push(self.teks)
        self.teks = self.redo_stack.pop()
        return True


def kasus_undo_redo():
    editor = EditorTeks()
    while True:
        print("\n--- Undo / Redo Editor Teks ---")
        print(f"Teks saat ini: \"{editor.teks}\"")
        print(f"(undo tersedia: {editor.undo_stack.size()} | redo tersedia: {editor.redo_stack.size()})")
        print("1. Tulis teks   2. Hapus N karakter terakhir")
        print("3. Undo         4. Redo         0. Kembali")
        pilihan = input("Pilih: ").strip()
        if pilihan == "1":
            editor.tulis(input("Teks yang ditulis: "))
        elif pilihan == "2":
            try:
                n = int(input("Jumlah karakter dihapus: "))
                if n <= 0:
                    raise ValueError
                editor.hapus(n)
            except ValueError:
                print("  Masukkan angka bulat > 0.")
        elif pilihan == "3":
            print("  Undo berhasil." if editor.undo() else "  Tidak ada yang bisa di-undo.")
        elif pilihan == "4":
            print("  Redo berhasil." if editor.redo() else "  Tidak ada yang bisa di-redo.")
        elif pilihan == "0":
            break
        else:
            print("  Pilihan tidak valid.")


def main():
    while True:
        print("\n=== STUDI KASUS STACK (DINAMIS) ===")
        print("1. Konversi infix -> postfix + evaluasi")
        print("2. Undo / Redo editor teks")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            kasus_postfix()
        elif pilihan == "2":
            kasus_undo_redo()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("  Pilihan tidak valid.")


if __name__ == "__main__":
    main()
