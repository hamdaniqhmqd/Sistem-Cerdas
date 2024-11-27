import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Title aplikasi
st.title("Aplikasi dengan Sidebar untuk Menampilkan Image, Dataset, dan Grafik")

# Import dataset
data = pd.read_csv("CarPrice_Assignment.csv")

# Sidebar menu
menu = st.sidebar.selectbox(
    "Pilih Menu",
    ["Image", "Dataset", "Grafik"]
)

if menu == "Image":
    # Menampilkan gambar
    st.header("Menampilkan Gambar")
    image = Image.open("output.png")
    st.image(image, caption="Gambar yang diunggah", use_container_width=True)

elif menu == "Dataset":
    # Menampilkan dataset
    st.header("Menampilkan Dataset")
    st.write("Dataset yang diunggah:")
    st.dataframe(data)

elif menu == "Grafik":
    # Menampilkan grafik
    st.header("Menampilkan Grafik")
    fig, ax = plt.subplots()
    ax.plot(data["carlength"], data["carwidth"], label="carwidth")
    ax.plot(data["carlength"], data["carheight"], label="carheight")
    ax.set_title("Grafik Line Chart")
    ax.legend()
    st.pyplot(fig)
