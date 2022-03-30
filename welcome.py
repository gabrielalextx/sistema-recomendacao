import streamlit as st
from multiapp import MultiApp
import home, recommendation, choice

welcome = MultiApp()

st.markdown("""
# Sistema de Recomendação de Jogos

Este é um sistema de recomendação desenvolvido pela equipe: Gabriel Alexander F. de L. Teixeira, Helder Melik Schramm, 
Vinicius Soares da Costa.

""")

welcome.add_app("Home", home.app)
welcome.add_app("Escolha", choice.app)
welcome.add_app("Recomendações", recommendation.app)


welcome.run()