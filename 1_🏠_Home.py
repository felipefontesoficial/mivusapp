import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="App Mivus | Mivus Academy"
)


logo = "caminho_para_sua_logo.png" 
st.sidebar.image(logo, use_column_width=True)

st.title("Olá, Querido Lendário 😀")
st.write("Agora, tudo o que você precisa estará organizado em um só lugar.")

