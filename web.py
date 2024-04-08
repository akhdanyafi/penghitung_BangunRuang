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
sisi = st.number_input("Masukkan sisi persegi:", 0 )

hitung_luas = st.button("hitung luas persegi")

if hitung_luas:
    luas_persegi = sisi * sisi
    st.write("luas persegi adalah",luas_persegi)

st.write("---")

#segitiga
st.write("Segitiga")
alas = st.number_input("Masukkan Alas Segitiga:",0)
tinggi = st.number_input("Masukkan Tinggi Segitiga:",0)

hitung_luas = st.button("hitung luas segitiga")

if hitung_luas:
    luas_sgitiga = (1/2) * alas * tinggi
    st.write("luas segitiga adalah:",luas_sgitiga)
