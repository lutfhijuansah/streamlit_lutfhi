import streamlit as st
import pandas as pd

def tampilkan_machine_learning():
    st.header("🤖 Prediksi Sederhana Churn")

    # Load data
    @st.cache_data
    def load_data():
        data = pd.read_csv('bank_churn.csv')  # Sesuaikan nama file
        return data

    data = load_data()

    st.subheader("Sekilas Data")
    st.dataframe(data.head())

    # Form input pengguna
    st.subheader("Input Data Nasabah")
    with st.form("form_prediksi"):
        gender = st.selectbox("Pilih Gender", options=data['Gender'].unique())
        geography = st.selectbox("Pilih Geography", options=data['Geography'].unique())
        age = st.slider("Umur", 18, 100, 30)
        credit_score = st.slider("Credit Score", 300, 900, 600)
        
        submitted = st.form_submit_button("Prediksi")

    # Logika Prediksi Sederhana
    if submitted:
        churn_risk = 0  # default: tidak churn

        if credit_score < 500 and age > 50:
            churn_risk = 1  # rawan churn

        # Output hasil prediksi
        st.subheader("Hasil Prediksi")
        if churn_risk == 1:
            st.error("⚠️ Nasabah berisiko Churn!")
        else:
            st.success("✅ Nasabah cenderung Bertahan.")

    st.markdown("---")
    st.info("Note: Ini hanya prediksi sederhana berbasis rule, bukan model machine learning sebenarnya.")

