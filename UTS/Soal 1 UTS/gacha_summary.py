import streamlit as st
from history_gacha import history_gacha

st.title("Gacha History Tracker")

# TODO 1: Buat pilihan pengurutan waktu dengan st.radio () dengan pilihan "Terbaru (Descending)" atau "Terlama (Ascending)"
urutan = ...

# TODO 2: Tentukan is_descending berdasarkan value urutan
if ...:
    is_descending = ...
else:
    is_descending = ...

# TODO 3: Urutkan data berdasarkan timestamp
sorted_history = list(history_gacha)
n = len(sorted_history)

# GUNAKAN BUBBLE SORT
# 1. Buat nested loop untuk mengambil data 2 item
# 2. Bandingkan nilai "timestamp" antara kedua elemen tersebut berdasarkan status is_descending
# 3. Lakukan penukaran posisi elemen (swapping) jika posisi timestamp tidak sesuai dengan urutan yang dipilih

# TODO 4: Kelompokkan item bintang 5 dan 4 menggunakan perulangan for biasa
five_stars = []
four_stars = []

for item in history_gacha:
    #jika 5 star tambahkan ke five_stars
    #jika 4 star tambahkan ke four_stars
    pass

# TODO 5: Tampilkan Summary Pity & Drop
st.subheader("Summary Pity & Drop")
col1, col2, col3 = st.columns(3)
col1.metric("Total Pull", ...) #total pull
col2.metric("Total Bintang 5 ", ...) #total 5 star
col3.metric("Total Bintang 4 ", ...) #total 4 star

# TODO 6: Menampilkan Summary Nama-Nama Bintang 5 & 4

with st.expander("Lihat Summary 5 star & 4 star"):
    # Tampilan Bintang 5
    
    # Tampilan Bintang 4

    pass


st.divider()

# TODO 7: Tampilkan History Pull
st.subheader("History Pull")
for data in sorted_history:

    # jika bintang 5 tampilkan dengan st.warning

    # jika bintang 4 tampilkan dengan st.success

    # selain itu dengan st.info

    # FORMAT TAMPILAN DATA: <Nama Item> (Rarity: <Rarity> star) — <Timestamp>
    pass
    
