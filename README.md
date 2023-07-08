# Gomoku Bot Competition
Made by Dimas Faidh Muzaki

## Latar Belakang
Masih ingatkah kalian dengan tugas besar 1 stima kalian ? Kalian diminta membuat bot untuk memenangkan sebuah game kapal perasng. Tujuan dari task ini adalah sama, yaitu membuat bot dengan menggunakan algoritma greedy. Tapi pada kali ini game yang berusaha dimenangkan adalah Gomoku atau sering disebut five in a row. Berbeda dengan task lainnya, task ini akan membandingkan hasil kerja kalian dengan teman seleksi lainnya dalam sebuah kompetisi. Jadi distribusi skor akan berdasarkan pemenang dari kompetisi. Maka kalian harus bisa membuat bot seoptimal mungkin. Good Luck Have Fun!

## Spesifikasi
* Pada task ini kalian akan membuat sebuah Bot Gomoku memanfaatkan algoritma Greedy
* Bot dibuat dengan mengoverwrite kelas Bot13521xxx di dalam `bots/bot_13521xxx.py`. Silakan ubah nilai xxx dengan NIM kalian. Selain itu, ubah nilai atribut NIM menjadi NIM kalian
* Pastikan method-method lain selain get_input tidak berubah di dalam submisi kalian.
* Silakan modifikasi method get_input sesuai strategi kalian. Pastikan keluarannya adalah sebuah string "x,y" yang menggambarkan koordinat board untuk menaruh pion
* Berikut spesifikasi dari game Connect Four yang akan digunakan:
  1. Ukurang board adalah 8x8
  2. Thinking time dari bot maksimal 3 detik. Setelah timeout, bot akan dianggap kalah
* **Dilarang** mengambil atau menggunakan algoritma dari internet ataupun teman seleksi lainnya. 
* **Dilarang** mengimplementasikan algoritma selain metode Greedy
* Peserta yang melanggar aturan diatas akan diskualifikasi dari kompetisi dan tidak dapat mendapatkan skor.

## Teknis Kompetisi
* Kompetisi dimulai ketika submisi pertama dilakukan
* Kompetisi ini akan berlangsung selama keberjalanan seleksi asisten IRK
* Pemenang dari kompetisi akan ditentukan dari peserta yang berhasil mengumpulkan poin terbanyak di akhir kompetisi (**berbeda dengan poin seleksi**)
* Peserta dapat mengumpulkan poin berdasarkan **peringkat** dari memenangkan **daily tournament** yang akan diadakan 5 kali dalam seminggu (jam 12:00), pada hari kerja. 
* **Daily tournament** menggunakan format round-robin tournament. Dengan begitu, semua bot submisi akan saling bertanding satu kali.
* Pada setiap pertandingan, bot yang menang akan mendapat 2 poin, sedangkan bot yang kalah tidak mendapat poin. Jika hasil pertandingan adalah seri maka kedua bot akan mendapatkan masing-masing 1 poin.
* Hasil peringkat pada tiap turnamen akan menentukan perolehan poin peserta dalam kompetisi ini.
* Poin kompetisi dilihat dari peringkat dan jumlah bot yang berpartisipasi dalam turnamen. Peringkat pertama akan mendapatkan n poin kompetisi, dengan n adalah jumlah partisipan. Peringkat selanjutnya mendapat poin kompetisi sebesar n-1 sampai peringkat terakhir mendapat poin kompetisi sebesar 1.
* Bila terdapat kesamaan pada poin turnamen maka akan mereka yang berpoin turnamen sama akan mendapat poin kompetisi tertinggi yang mungkin.

* Anda bingung? Coba lihat contoh ini.
### Turnamen Senin

| Posisi | Bot | Menang | Kalah | Seri | Poin turnamen | Poin Kompetisi |   
| ----------- | ----- | ----------- | ----------- | ----------- | ----------- | ----------- |
| 1   | Bot13521999 | 3 | 0 | 0 | 6 | 4
| 2   | Bot13521888 | 1 | 1 | 1 | 3 | 3
| 3   | Bot13521777 | 1 | 1 | 1 | 3 | 3
| 4   | Bot13521666 | 0 | 0 | 3 | 0 | 1

Scoreboard Kompetisi
| Posisi | Peserta | Poin Kompetisi |
| ----------- | ----------- | - |
| 1   | 13521999 | 4 |
| 2   | 13521888 | 3 |
| 3   | 13521777 | 3 |
| 4   | 13521666 | 2 |

### Turnamen Selasa
| Posisi | Bot | Menang | Kalah | Seri | Poin turnamen | Poin Kompetisi |   
| ----------- | ----- | ----------- | ----------- | ----------- | ----------- | ----------- |
| 1   | Bot13521888 | 4 | 0 | 0 | 8 | 5
| 2   | Bot13521666 | 3 | 0 | 1 | 6 | 4
| 3   | Bot13521999 | 2 | 0 | 2 | 4 | 3
| 4   | Bot13521555 | 1 | 0 | 3 | 2 | 2
| 4   | Bot13521777 | 0 | 0 | 4 | 0 | 1

Scoreboard Kompetisi
| Posisi | Peserta | Poin Kompetisi |
| ----------- | ----------- | - |
| 1   | 13521888 | 8 |
| 2   | 13521999 | 7 |
| 3   | 13521666 | 6 |
| 4   | 13521777 | 4 |
| 5   | 13521555 | 2 |

*p.s. Lihat bahwa lebih baik ikut berkompetisi sesegera mungkin

* Scoreboard kompetisi dan informasi **Daily tournament** dapat dilihat pada [sheet berikut]()
* Berikut distribusi skor pada pemenang kompetisi setelah kompetisi berakhir:

| Posisi | Poin Seleksi |
| ----------- | ----------- |
| 1   | 2500 |
| 2   | 2250 |
| 3   | 2000 |
| 4   | 1750 |
| 5   | 1500 |
| 6   | 1250 |
| 7   | 1000 |
| 8 | 750 |
| 9 - dst. | 500 |

## Pengerjaan & Pengumpulan Bot
1. Clone repository ini pada sebuah repository private pada github Anda dan invite `maspaitujaki` ke dalam repository tersebut.
3. Submisi bot pada website dan lakukan konfirmkasi ke LINE @oohmasdim.
4. Memberikan tag `vn` pada commit terakhir Anda setiap kali ingin melakukan submisi bot dengan n adalah urutan submisi keberapa. (contoh: `v1` untuk submisi pertama)
5. Setiap peserta maksimal hanya dapat melakukan submisi bot sebanyak 5x, jadi pastikan bot yang dikumpulkan tidak ada error atau bug.
6. Peserta yang mengumpulkan bot setelah jam 12.00 WIB siang tidak dapat mengikuti **Daily tournament** hari tersebut.
7. Jika ada pertanyaan silahkan buat issues di [repository original](https://github.com/maspaitujaki/Gomoku_IRK)

## Credit
Original game by [junxiaosong](https://github.com/junxiaosong/AlphaZero_Gomoku)

Thanks to Kak Jonathan CJ IRK'19
