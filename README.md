# Winbox Installer
inspirasi dari https://github.com/mriza

## Deskripsi

Skrip ini bertujuan untuk menginstal dan menghapus aplikasi Winbox di sistem Linux menggunakan Python. Skrip ini akan mengunduh dependensi yang diperlukan, mengunduh Winbox dari situs resmi Mikrotik, menyalin file yang diperlukan ke direktori yang tepat, dan membuat peluncur aplikasi.

## Persyaratan
- Python 3.x
- Hak akses superuser (root) untuk menginstal dan menghapus file di direktori sistem

## Instalasi Dependensi
Sebelum menjalankan skrip, pastikan Anda telah menginstal Python 3 dan library `requests`. Anda dapat menginstal library `requests` dengan perintah berikut:

```bash
pip3 install requests
```


#Menginstal Winbox
Untuk menginstal Winbox, jalankan perintah berikut:
```
sudo python3 betmenb0x.py install
```
#Menghapus Winbox
Untuk menghapus Winbox, jalankan perintah berikut:
```
sudo python3 betmenb0x.py remove
```

#Struktur Proyek
```
betmenb0x/
├── betmenb0x.py
├── winbox.sh
├── icons/
│   ├── winbox-16.png
│   ├── winbox-32.png
│   └── winbox-48.png
└── README.md

    betmenb0x.py: Skrip utama untuk menginstal dan menghapus Winbox.
    winbox.sh: Skrip shell yang menjalankan Winbox menggunakan Wine.
    icons/: Direktori yang berisi ikon-ikon Winbox untuk peluncur aplikasi.
    README.md: Dokumentasi proyek.
```
**LICENSE**
MIT License

Copyright (c) [2024], [betmen-n-dgeng]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
