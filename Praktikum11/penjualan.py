
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Visualisasi Data Penjualan dari Excel dengan Matplotlib")

# Upload file Excel
uploaded_file = st.file_uploader("Unggah file Excel (.xlsx)", type=["xlsx"])

if uploaded_file is not None:

    # Membaca file Excel
    df = pd.read_excel(uploaded_file)

    st.subheader("Data Penjualan")
    st.dataframe(df)

    # Membuat figure dengan 4 grafik
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    fig.suptitle(
        'Visualisasi Data Penjualan Produk',
        fontsize=14,
        fontweight='bold'
    )

    # 1. Grafik garis tren penjualan
    axes[0, 0].plot(
        df['Bulan'], df['Produk_A'],
        marker='o', label='Produk A'
    )

    axes[0, 0].plot(
        df['Bulan'], df['Produk_B'],
        marker='s', label='Produk B'
    )

    axes[0, 0].plot(
        df['Bulan'], df['Produk_C'],
        marker='^', label='Produk C'
    )

    axes[0, 0].set_title('Tren Penjualan Bulanan')
    axes[0, 0].legend()
    axes[0, 0].grid(True, linestyle='--', alpha=0.6)

    # 2. Grafik batang penjualan Produk A
    axes[0, 1].bar(
        df['Bulan'], df['Produk_A'],
        color='skyblue', edgecolor='black'
    )

    axes[0, 1].set_title('Penjualan Produk A')
    axes[0, 1].grid(axis='y', linestyle='--', alpha=0.6)

    # 3. Scatter plot korelasi Produk A dan B
    axes[1, 0].scatter(
        df['Produk_A'], df['Produk_B'],
        color='orange', s=80, alpha=0.7,
        edgecolor='black'
    )

    axes[1, 0].set_title('Korelasi Produk A dan B')
    axes[1, 0].set_xlabel('Produk A')
    axes[1, 0].set_ylabel('Produk B')
    axes[1, 0].grid(True, linestyle='--', alpha=0.5)

    # 4. Histogram distribusi Produk C
    axes[1, 1].hist(
        df['Produk_C'], bins=6,
        color='lightgreen', edgecolor='black',
        rwidth=0.9
    )

    axes[1, 1].set_title('Distribusi Penjualan Produk C')
    axes[1, 1].grid(axis='y', linestyle='--', alpha=0.5)

    # Mengatur jarak grafik
    plt.tight_layout(rect=[0, 0, 1, 0.96])

    # Menampilkan grafik
    st.pyplot(fig)

else:
    st.info("Silakan unggah file Excel terlebih dahulu.")
