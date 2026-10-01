import streamlit as st
import pandas as pd

# --- Title ---
st.title("Pengeluaran Anak Kos 71251177")


# --- Input Uang Bulanan ---
st.subheader("Uang Bulanan")
uang_bulanan = st.number_input("Uang Bulanan", min_value=0, step=1000)


# --- Input Pengeluaran ---
st.subheader("Pengeluaran Bulanan")
makanan = st.number_input("Makanan", min_value=0, step=1000)
kos = st.number_input("Kos", min_value=0, step=1000)
transportasi = st.number_input("Transportasi", min_value=0, step=1000)
internet = st.number_input("internet", min_value=0, step=1000)
hiburan = st.number_input("Hiburan", min_value=0, step=1000)

# --- Tombol Ngitung Pengeluaran ---
if st.button("Hitung Pengeluaran"):

    # --- Ngitung Total Pengeluaran ---
    total_pengeluaran = (
        makanan + kos + transportasi + internet + hiburan
    )

    # --- Ngitung Sisa Uang ---
    sisa_uang = uang_bulanan - total_pengeluaran


    # --- Menampilkan Hasil Perhitungan ---
    st.subheader("Ringkasan Keuangan")
    kolom1, kolom2, kolom3 = st.columns(3)
    with kolom1:
        st.metric(
            # Tampilin uang bulanan di sini
            "Uang Bulanan", f"Rp{uang_bulanan:,.0f}"
        )
    with kolom2:
        st.metric(
            # Tampilin total pengeluaran di sini
            "Total Pengeluaran", f"Rp{total_pengeluaran:,.0f}"
        )
    with kolom3:
        st.metric(
            # Tampilin sisa uang di sini
            "Sisa Uang", f"Rp{sisa_uang:,.0f}"
        )


    # --- Kondisi Keuangan ---
    st.subheader("Kondisi Keuangan")

    # Kondisi 1
    if sisa_uang > 0:
        st.success("Keuanganmu masih aman bulan ini")

    # Kondisi 2
    elif sisa_uang == 0:
        st.warning("Uangmu habis :(")

    # Kondisi 3
    else:
        st.error("Pengeluaranmu melebihi uang bulanan!")


    # --- Data Pengeluaran ---
    # Ini gausah diubah! 
    # Udah kubantu bikinin, tinggal dipake aja
    data_pengeluaran = {
        "Kategori": [
            "Makanan",
            "Kos",
            "Transportasi",
            "Internet/Pulsa",
            "Hiburan"
        ],
        "Pengeluaran": [
            makanan,
            kos,
            transportasi,
            internet,
            hiburan
        ]
    }

    df_pengeluaran = pd.DataFrame(data_pengeluaran)

    # --- Pengeluaran Terbesar ---
    nilai_terbesar = max(
        makanan,
        kos,
        transportasi,
        internet,
        hiburan
    )

    st.subheader("Pengeluaran Terbesar")
    pengeluaran_terbesar = []
    if makanan == nilai_terbesar:
        pengeluaran_terbesar.append("Makanan")

    if kos == nilai_terbesar:
        pengeluaran_terbesar.append("Kos")

    if transportasi == nilai_terbesar:
        pengeluaran_terbesar.append("Transportasi")

    if internet == nilai_terbesar:
        pengeluaran_terbesar.append("Internet")

    if hiburan == nilai_terbesar:
        pengeluaran_terbesar.append("Hiburan")

    # --- Grafik Pengeluaran ---
    st.subheader("Grafik Pengeluaran")
    st.bar_chart(df_pengeluaran.set_index("Kategori"))