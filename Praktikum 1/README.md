# Penjelasan Kode Jawaban Praktikum 1

## Soal
https://github.com/mahirahyam/Tugas-Praktikum-Otomata/blob/main/Praktikum%201/praktikum-1-otomata.png
Buatlah program computer yang dapat membaca inputan berupa program computer lain, dan dapat menghasilkan output berupa token-token (string-string yang terbaca) dan mengelompokkannya sesuai dengan sifat string tersebut:
- Reserve words
- Simbol dan tanda baca
- Variabel
- Kalimat matematika (persamaan, fungsi, dsb)

## Jawaban & Penjelasan
```
def lexical_analyzer(code):
    reserved_words = {'if', 'else', 'while', 'for', 'return', 'int', 'float', 'print', 'def', 'class'}
    math_operators = r'[+\-*/%=<>!]=?'
    symbols = r'[()\[\]{};,.]'
    variables = r'[a-zA-Z_][a-zA-Z0-9_]*'
    numbers = r'\d+(\.\d+)?'
```
Di bagian awal fungsi `lexical_analyzer`, kita mendefinisikan aturan menggunakan Regex (Regular Expression). Regex ini adalah cara kita merepresentasikan Finite Automata.
- reserved_words: Kumpulan kata kunci yang sudah ada di dalam bahasa pemrograman.
- math_operators: Mencari karakter matematika seperti +, -, atau operator gabungan seperti += atau ==.
- symbols: Mencari tanda baca seperti kurung () atau titik koma ;.
- variables: Aturannya adalah harus dimulai dengan huruf atau underscore, boleh diikuti angka.
- numbers: Mencari angka bulat maupun desimal.

```
master_pattern = re.compile(
        f'(?P<MATH>{math_operators})|'
        f'(?P<SYMBOL>{symbols})|'
        f'(?P<VAR>{variables})|'
        f'(?P<NUM>{numbers})'
    )

    results = {
        "Reserve Words": [],
        "Simbol & Tanda Baca": [],
        "Variabel": [],
        "Kalimat Matematika (Operator/Angka)": []
    }
```
Di `master_pattern`, semua aturan tadi disatukan menjadi satu. Penggunaan (?P<NAMA>...) disebut Named Groups. Ini memudahkan program untuk tahu kategori string tanpa harus menebak-nebak lagi.

`result` menampilkan list berdasarkan kategori yang diminta.

```
for match in master_pattern.finditer(code):
    token_type = match.lastgroup  # Mengambil nama label (MATH/VAR/dsb)
    value = match.group()         # Mengambil teks aslinya (misal: 'if')

    if token_type == 'VAR':
        # Cek apakah variabel tersebut sebenarnya adalah kata kunci cadangan
        if value in reserved_words:
            results["Reserve Words"].append(value)
        else:
            results["Variable"].append(value)
    elif token_type == 'SYMBOL':
        results["Simbol & Tanda Baca"].append(value)
    elif token_type == 'MATH' or token_type == 'NUM':
        # Menggabungkan operator dan angka sesuai permintaan soal (kalimat matematika)
        results["Kalimat Matematika (Operator/Angka)"].append(value)
```
`finditer(code)` menyisir string dari awal sampai akhir.

Jika tipenya VAR, kita cek lagi ke daftar reserved_words. Jika ada di sana, dia bukan variabel biasa.

Jika tipenya NUM atau MATH, mereka masuk ke kategori Kalimat Matematika.

```
while True:
    input_user = input("\nInput Kode: ")
    if input_user.lower() == 'exit':
        break
    
    hasil = lexical_analyzer(input_user)
    
    for kategori, token_list in hasil.items():
        # Menghapus duplikat agar output bersih
        unique_tokens = list(dict.fromkeys(token_list)) 
        print(f"{kategori:35}: {', '.join(unique_tokens) if unique_tokens else '-'}")
```
`dict.fromkeys(token_list)`: Teknik cepat di Python untuk menghapus duplikat dalam list sambil tetap menjaga urutannya. Misalnya, kalau input a = a + 1, variabel a hanya akan ditampilkan sekali di hasil analisis agar tidak berantakan.

`f"{kategori:35}"` adalah format string agar outputnya rapi rata kiri dengan lebar 35 karakter.
