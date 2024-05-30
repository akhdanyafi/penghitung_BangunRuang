import streamlit as st

#st.write: buat nulis pesan atau info di web
st.write("""
# Aplikasi penghitung luas bangun ruang
Selamat datang di aplikasi penghitung bangun ruang \n
*this app is made by AkhdanGanteng* \n
--- \n       
""")

#persegi
st.write("Persegi")
sisi = st.number_input("Masukkan sisi persegi: ", 0 )

hitung_luas = st.button("hitung luas persegi")

if hitung_luas:
    luas_persegi = sisi * sisi
    st.success("luas persegi adalah: ",luas_persegi)

st.write("---")

#segitiga
st.write("Segitiga")
alas = st.number_input("Masukkan Alas Segitiga:",0)
tinggi = st.number_input("Masukkan Tinggi Segitiga:",0)

hitung_luas_segitiga = st.button("hitung luas segitiga")

if hitung_luas_segitiga:
    luas_sgitiga = (1/2) * alas * tinggi
    st.success("luas segitiga adalah:",luas_sgitiga)

st.write("---")

#persegi panjang
st.write("Persegi Panjang")
panjang = st.number_input("Masukkan panjang segitiga", min_value = 0, max_value = 999999999999)
lebar = st.number_input("Masukkan lebar", min_value = 0, max_value = 99999999999)

hitung_luas_PersegiPanjang = st.button("hitung luas persegi panjang")

if hitung_luas_PersegiPanjang:
    luas_persegiPanjang = panjang * lebar
    st.success(f"Luas Persegi Panjang: {luas_persegiPanjang}")
