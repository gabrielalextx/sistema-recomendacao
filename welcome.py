import streamlit as st
from multiapp import MultiApp
from apps import home, recommendation, choice

welcome = MultiApp()

st.markdown("""
# Sistema de Recomendação de Jogos

Este é um sistema de recomendação desenvolvido pela equipe: Gabriel Alexander, Helder Melik, Vinicius Soares.

""")

welcome.add_app("Home", home.app)
welcome.add_app("Escolha", choice.app)
welcome.add_app("Recomendações", recommendation.app)


welcome.run()