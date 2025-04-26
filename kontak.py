import streamlit as st

def tampilkan_kontak():
    st.title("Kontak")
    st.write("Hubungi saya melalui tautan berikut:")

    #Linkedin
    st.markdown(
        "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/lutfhijuansah)"
    )
    
    #GitHub
    st.markdown(
        "[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue)](https://github.com/lutfhijuansah/streamlit_lutfhi)"
    )

    #Email
    st.write("📧Email: juansah.lutfhi@gmail.com")
