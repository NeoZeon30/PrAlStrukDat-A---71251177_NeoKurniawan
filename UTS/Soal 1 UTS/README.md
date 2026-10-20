# Ujian Tengah Semester (UTS) Pemrograman
**Topik:** Pemrosesan Koleksi Data, Algoritma Pengurutan Manual, dan Interaktif Dashboard Streamlit  
**Kasus:** Gacha History Tracker (Genshin Impact & Honkai: Star Rail)

---

## Deskripsi Kasus
Kamu diminta untuk membuat aplikasi web interaktif menggunakan **Streamlit** untuk melacak riwayat *pull gacha* pemain. Aplikasi ini akan membaca data riwayat dari berkas `history_gacha.py`, melakukan pengurutan data berdasarkan waktu (*timestamp*), menghitung ringkasan perolehan item bintang 5 dan bintang 4, serta menampilkan riwayat *pull* pada *dashboard*.

---

## Ketentuan Pengerjaan (PENTING)
1. **Dilarang menggunakan fungsi/metode pengurutan bawaan Python** seperti `sorted()` atau `.sort()`. Pengurutan data WAJIB dibuat secara manual menggunakan algoritma pengurutan (misalnya **Bubble Sort**, **Selection Sort**, atau **Insertion Sort**).
2. **Dilarang membuat fungsi (*def*) buatan sendiri** maupun menggunakan fungsi lambda.
3. **Dilarang menggunakan *Ternary Operator*** (seperti `x if condition else y`). Gunakan struktur blok bercabang `if-else` standar.
4. **Dilarang menggunakan *List Comprehension*** untuk proses pengelompokan data. Gunakan perulangan `for` biasa.
5. Seluruh logika aplikasi dikerjakan langsung pada berkas utama `app.py` dengan mengimpor modul data dari `history_gacha.py`.

---

## Spesifikasi Kebutuhan Sistem

### 1. Fitur Pengurutan Data (Algoritma Manual)
* Tampilkan kontrol pilihan tunggal (*radio button*) dengan label `"Urutkan Berdasarkan Waktu Pull:"` yang memiliki opsi:
  * `"Terbaru (Descending)"`
  * `"Terlama (Ascending)"`
* Tentukan status arah pengurutan menggunakan struktur percabangan `if-else` biasa.
* Buat salinan list data riwayat gacha, lalu urutkan list tersebut berdasarkan tanggal dan jam (*timestamp*) secara manual menggunakan algoritma **Bubble Sort** (atau algoritma pengurutan iteratif lainnya) tanpa memanggil fungsi terpisah.

### 2. Agregasi & Ringkasan (Summary)
* Lakukan iterasi pada data riwayat gacha menggunakan perulangan biasa untuk mengelompokkan nama item berdasarkan tingkat kelangkaannya (*rarity*):
  * Kelompokkan nama item bintang 5 ke dalam list khusus.
  * Kelompokkan nama item bintang 4 ke dalam list khusus.
* Tampilkan bagian ringkasan dengan judul `"Summary Pity & Drop"`.
* Susun tampilan metrik dalam 3 kolom sejajar:
  * **Kolom 1**: Menampilkan total seluruh riwayat *pull*.
  * **Kolom 2**: Menampilkan total perolehan item bintang 5.
  * **Kolom 3**: Menampilkan total perolehan item bintang 4.
* Buat komponen penutup/pembuka (*expander*) dengan label `"Lihat Summary 5 star & 4 star"` yang berisi:
  * Daftar nama item bintang 5 yang didapatkan (dipisahkan koma). Jika tidak ada, tampilkan pesan bahwa bintang 5 belum ada.
  * Daftar nama item bintang 4 yang didapatkan (dipisahkan koma). Jika tidak ada, tampilkan pesan bahwa bintang 4 belum ada.

### 3. Visualisasi History Pull
* Tambahkan garis pemisah visual sebelum bagian riwayat.
* Tampilkan bagian riwayat dengan judul `"History Pull"`.
* Tampilkan seluruh data riwayat yang telah terurut manual menggunakan perulangan biasa dengan ketentuan warna/elemen tampilan berdasarkan *rarity*:
  * **Rarity 5**: Gunakan elemen pesan sukses (*success*).
  * **Rarity 4**: Gunakan elemen pesan informasi (*info*).
  * **Rarity 3**: Gunakan elemen teks standar (*write*).
* Tampilkan setiap baris riwayat dengan format: `<Nama Item> (Rarity: <Rarity> star) — <Timestamp>`
