"""
Studi Kasus Queue (DINAMIS / LINKED LIST)
  1. Antrian printer (print spooler)
  2. Penjadwalan CPU Round Robin
"""
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE, "..", "..", "Library Queue", "Dinamis"))

from queue_dinamis import QueueDinamis  # noqa: E402


def input_int(prompt, minimum=None):
    while True:
        try:
            nilai = int(input(prompt))
        except ValueError:
            print("  Input harus berupa angka bulat.")
            continue
        if minimum is not None and nilai < minimum:
            print(f"  Nilai minimal {minimum}.")
            continue
        return nilai


# ---------- Kasus 1: Antrian printer ----------
def kasus_printer():
    antrian = QueueDinamis()
    while True:
        print("\n--- ANTRIAN PRINTER ---")
        print("1. Tambah dokumen")
        print("2. Cetak dokumen berikutnya")
        print("3. Lihat antrian")
        print("0. Kembali")
        pilihan = input("Pilih: ").strip()
        try:
            if pilihan == "1":
                nama = input("Nama dokumen: ").strip() or "dokumen"
                halaman = input_int("Jumlah halaman: ", 1)
                antrian.enqueue((nama, halaman))
                print(f"  '{nama}' ({halaman} hlm) masuk antrian.")
            elif pilihan == "2":
                nama, halaman = antrian.dequeue()
                print(f"  Mencetak '{nama}' ({halaman} halaman)... selesai.")
            elif pilihan == "3":
                if antrian.is_empty():
                    print("  (tidak ada dokumen)")
                else:
                    total = 0
                    for i, (nama, halaman) in enumerate(antrian.to_list(), start=1):
                        print(f"  {i}. {nama} ({halaman} hlm)")
                        total += halaman
                    print(f"  Total: {antrian.size()} dokumen, {total} halaman")
            elif pilihan == "0":
                break
            else:
                print("  Pilihan tidak valid.")
        except IndexError:
            print("  Tidak ada dokumen dalam antrian.")


# ---------- Kasus 2: Round Robin ----------
def round_robin(proses, quantum):
    """proses: list (nama, burst). Semua proses tiba pada waktu 0."""
    antrian = QueueDinamis()
    for nama, burst in proses:
        antrian.enqueue({"nama": nama, "burst": burst, "sisa": burst})
    waktu = 0
    log = []
    hasil = []
    while not antrian.is_empty():
        p = antrian.dequeue()
        jalan = min(quantum, p["sisa"])
        log.append((p["nama"], waktu, waktu + jalan))
        waktu += jalan
        p["sisa"] -= jalan
        if p["sisa"] > 0:
            antrian.enqueue(p)  # belum selesai: kembali ke belakang antrian
        else:
            p["selesai"] = waktu
            hasil.append(p)
    return log, hasil


def kasus_round_robin():
    print("\n--- PENJADWALAN CPU ROUND ROBIN ---")
    jumlah = input_int("Jumlah proses: ", 1)
    proses = []
    for i in range(1, jumlah + 1):
        nama = input(f"  Nama proses ke-{i} [P{i}]: ").strip() or f"P{i}"
        burst = input_int(f"  Burst time {nama}: ", 1)
        proses.append((nama, burst))
    quantum = input_int("Time quantum: ", 1)

    log, hasil = round_robin(proses, quantum)

    print("\n  Urutan eksekusi (Gantt):")
    for nama, mulai, akhir in log:
        print(f"    {mulai:>3} - {akhir:<3} : {nama}")

    print(f"\n  {'Proses':<10}{'Burst':>6}{'Selesai':>9}{'Turnaround':>12}{'Waiting':>9}")
    total_tat = total_wait = 0
    for p in hasil:
        tat = p["selesai"]
        wait = tat - p["burst"]
        total_tat += tat
        total_wait += wait
        print(f"  {p['nama']:<10}{p['burst']:>6}{p['selesai']:>9}{tat:>12}{wait:>9}")
    n = len(hasil)
    print(f"\n  Rata-rata turnaround: {total_tat / n:.2f}")
    print(f"  Rata-rata waiting   : {total_wait / n:.2f}")


def main():
    while True:
        print("\n=== STUDI KASUS QUEUE (DINAMIS) ===")
        print("1. Antrian printer")
        print("2. Penjadwalan CPU Round Robin")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            kasus_printer()
        elif pilihan == "2":
            kasus_round_robin()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("  Pilihan tidak valid.")


if __name__ == "__main__":
    main()
