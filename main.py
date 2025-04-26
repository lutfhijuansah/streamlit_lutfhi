import streamlit as st

st.set_page_config(page_title="Portofolio", layout="wide", page_icon=":rocket:")
st.title("Portofolio Saya")
st.header("Data Scientist & Data Analyst")

st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman", ["Tentang Saya", "Project", "Machine Learning", "Kontak"])

if page == "Tentang Saya":
    import tentang_saya
    tentang_saya.tampilkan_tentang_saya()
elif page == "Kontak":
    import kontak
    kontak.tampilkan_kontak()
elif page == "Project":
    import project
    project.tampilkan_project()
elif page == "Machine Learning":
    import machine_learning
    machine_learning.tampilkan_machine_learning()



