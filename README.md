# Stack & Queue (Python)

- **Statis**  = array / list berukuran tetap (kapasitas ditentukan di awal; queue memakai circular array)
- **Dinamis** = linked list (ukuran tumbuh sesuai kebutuhan)

## Struktur
```
Library Stack/        stack_statis.py, stack_dinamis.py      (class)
Library Queue/        queue_statis.py, queue_dinamis.py      (class)
Operasi Stack/        menu push, pop, peek, display, dll
Operasi Queue/        menu enqueue, dequeue, front, rear, dll
Study Kasus Stack/    Statis : kurung seimbang, palindrom
                      Dinamis: infix->postfix + evaluasi, undo/redo
Study Kasus Queue/    Statis : antrian bank, hot potato
                      Dinamis: antrian printer, round robin
```
Setiap folder punya subfolder `Statis` dan `Dinamis`.

## Cara menjalankan
Butuh Python 3.6+. Dari folder utama:
```
python "Operasi Stack/Statis/operasi_stack_statis.py"
python "Study Kasus Queue/Dinamis/studi_kasus_queue_dinamis.py"
```
File library bisa dites sendiri: `python "Library Stack/Statis/stack_statis.py"`

File Operasi dan Study Kasus otomatis mengimpor library dari folder Library,
jadi struktur folder jangan diubah.
