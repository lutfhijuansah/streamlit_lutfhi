import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def tampilkan_project():
    st.title("Analisis Churn Nasabah Bank")
    st.write("Proyek ini bertujuan untuk memahami faktor-faktor yang mempengaruhi nasabah keluar (churn) dari layanan bank, menggunakan teknik analisis data dan machine learning.")
    
    # Load dataset
    df = pd.read_csv('bank_churn.csv')
    
    st.header("Gambaran Umum Dataset")
    st.dataframe(df.head())

    st.markdown("""
    - **Jumlah Data**: {} baris
    - **Jumlah Fitur**: {} kolom
    """.format(df.shape[0], df.shape[1]))
    
    st.header("Visualisasi Data")

    # Tabs untuk memisahkan visualisasi
    tab1, tab2, tab3 = st.tabs(["Distribusi Gender", "Proporsi Churn", "Distribusi Usia"])

    with tab1:
        st.subheader("Distribusi Gender Nasabah")
        fig, ax = plt.subplots()
        sns.countplot(data=df, x="Gender", palette="Set2", ax=ax)
        st.pyplot(fig)

    with tab2:
        st.subheader("Proporsi Nasabah Churn vs Tidak Churn")
        fig, ax = plt.subplots()
        sns.countplot(data=df, x="Exited", palette="pastel", ax=ax)
        ax.set_xticklabels(["Tidak Churn", "Churn"])
        st.pyplot(fig)

    with tab3:
        st.subheader("Distribusi Usia Nasabah")
        fig, ax = plt.subplots()
        sns.histplot(df['Age'], kde=True, color="skyblue")
        st.pyplot(fig)

    st.header("Filter Data")
    # Range usia
    min_age = int(df['Age'].min())
    max_age = int(df['Age'].max())
    age_range = st.slider('Pilih rentang usia:', min_age, max_age, (25, 50))
    st.write(f"Anda memilih rentang usia: {age_range}")

    # Tampilkan data yang difilter
    df_filtered = df[(df['Age'] >= age_range[0]) & (df['Age'] <= age_range[1])]
    st.dataframe(df_filtered)


