from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
import requests

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
}

st.set_page_config(page_title="Dashboard Katalog Buku", layout="wide")
st.title("Dashboard Katalog Buku")
st.write("Mengambil data buku melalui web scraping dan kurs GBP/IDR melalui REST API.")

jumlah_halaman = st.slider("Jumlah halaman katalog yang diambil", 1, 3, 2)

if st.button("Ambil Data dan Tampilkan Dashboard", type="primary"):
    data_buku = []

    for halaman in range(1, jumlah_halaman + 1):
        url = f"https://books.toscrape.com/catalogue/page-{halaman}.html"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        produk_list = soup.select("article.product_pod")
        for produk in produk_list:
            judul = produk.find("h3").find("a")["title"]

            harga_teks = produk.find("p", class_="price_color").text
            harga_bersih = harga_teks.replace("Â", "").replace("£", "").strip()
            harga_gbp = float(harga_bersih)

            rating_kelas = produk.find("p", class_="star-rating")["class"][1]
            rating = RATING_MAP[rating_kelas]

            ketersediaan = produk.find("p", class_="instock availability").text.strip()

            data_buku.append({
                "judul": judul,
                "harga_gbp": harga_gbp,
                "rating": rating,
                "ketersediaan": ketersediaan
            })

    response_kurs = requests.get("https://api.frankfurter.dev/v1/latest?base=GBP&symbols=IDR")
    data_kurs = response_kurs.json()
    kurs_idr = data_kurs["rates"]["IDR"]

    df = pd.DataFrame(data_buku)
    df["harga_idr"] = (df["harga_gbp"] * kurs_idr).round(2)

    st.subheader("Data Katalog Buku")
    st.caption(f"{len(df)} buku diambil dari {jumlah_halaman} halaman.")
    st.dataframe(df, use_container_width = True)
    st.subheader("Visualisasi")
    col1, col2 = st.columns(2)

    with col1:
        fig1, ax1 = plt.subplots()
        ax1.hist(df["harga_idr"], bins = 10, edgecolor = "black")
        ax1.set_title("Distribusi Harga Buku")
        ax1.set_xlabel("Harga (Rupiah)")
        ax1.set_ylabel("Jumlah Buku")
        ax1.grid(True, alpha=0.3)
        st.pyplot(fig1)

    with col2:
        fig2, ax2 = plt.subplots()
        jumlah_rating = df["rating"].value_counts().reindex([1,2,3,4,5], fill_value=0)
        ax2.bar(jumlah_rating.index, jumlah_rating.values)
        ax2.set_title("Jumlah Buku Berdasarkan Rating")
        ax2.set_xlabel("Rating")
        ax2.set_ylabel("Jumlah Buku")
        ax2.set_xticks([2,3,4,5])
        st.pyplot(fig2)