import streamlit as st

# Fungsi untuk menghitung nilai Z
def nilai_z(X, u=43, o=11):
    Z = (X - u) / o
    return Z

# Fungsi untuk menghitung nilai IQ
def nilai_iq(Z):
    iq = 100 + 15 * Z
    return iq

# Fungsi untuk menentukan kategori IQ
def outcome(iq):
    if 0 <= iq < 90:
        kategori = "Di bawah rata-rata"
    elif 90 <= iq < 110:
        kategori = "Rata-rata"
    else:
        kategori = "Di atas rata-rata"
    return kategori

# Fungsi utama Streamlit
def main():
    st.title("Aplikasi Perhitungan IQ")
    st.write("Masukkan skor mentah Anda untuk mengetahui nilai IQ dan kategorinya.")

    # Input skor mentah dari pengguna
    X = st.number_input("Masukkan Skor Mentah Anda:", min_value=0, max_value=200, step=1)

    if st.button("Hitung"):
        Z = nilai_z(X)
        iq = nilai_iq(Z)
        iq_bulat = round(iq)
        kategori = outcome(iq_bulat)

        # Menampilkan hasil
        st.write(f"**Nilai Z Anda adalah:** {Z:.2f}")
        st.write(f"**Nilai IQ Anda adalah:** {iq:.2f}")
        st.write(f"**Nilai IQ Anda yang dibulatkan adalah:** {iq_bulat}")
        st.write(f"**Kategori:** {kategori}")

# Menjalankan aplikasi
if __name__ == "__main__":
    main()
