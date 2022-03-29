import streamlit as st
import apps.main as main

def app():
    st.title("Escolha")
    st.write("Por favor, avalie cada um dos jogos com notas de 0 a 10:")
    main.main()