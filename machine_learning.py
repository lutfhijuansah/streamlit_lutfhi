import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

def tampilkan_machine_learning():
    st.title("Prediksi Churn Menggunakan Machine Learning")

    # Load data
    @st.cache_data
    def load_data():
        data = pd.read_csv('bank_churn.csv')
        return data

    data = load_data()

    st.subheader("Sekilas Data")
    st.dataframe(data.head())

    # Preprocessing sederhana
    le_gender = LabelEncoder()
    le_geo = LabelEncoder()

    data['Gender'] = le_gender.fit_transform(data['Gender'])
    data['Geography'] = le_geo.fit_transform(data['Geography'])

    X = data[['Gender', 'Geography', 'Age', 'CreditScore']]
    y = data['Exited']  # Sesuaikan, kolom churn biasanya 'Exited'

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Form input pengguna
    st.subheader("Input Data Nasabah")
    with st.form("form_prediksi"):
        gender = st.selectbox("Pilih Gender", options=le_gender.classes_)
        geography = st.selectbox("Pilih Geography", options=le_geo.classes_)
        age = st.slider("Umur", 18, 100, 30)
        credit_score = st.slider("Credit Score", 300, 900, 600)
        
        submitted = st.form_submit_button("Prediksi")

    # Prediksi
    if submitted:
        input_data = pd.DataFrame({
            'Gender': [le_gender.transform([gender])[0]],
            'Geography': [le_geo.transform([geography])[0]],
            'Age': [age],
            'CreditScore': [credit_score]
        })

        prediction = model.predict(input_data)[0]

        st.subheader("Hasil Prediksi")
        if prediction == 1:
            st.error("⚠️ Nasabah berisiko Churn!")
        else:
            st.success("✅ Nasabah cenderung Bertahan.")

    st.markdown("---")
    st.info("Note: Model Machine Learning yang digunakan adalah Logistic Regression.")

