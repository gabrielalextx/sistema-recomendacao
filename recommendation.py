import pickle

import streamlit as st
from pisson import recommend

def app():
    st.title("Recomendações")
    st.subheader("Aqui estão suas recomendações:")

    player_file = open("player.txt", "rb")
    player = pickle.load(player_file)
    user_list_file = open("list_users.txt", "rb")
    user_list = pickle.load(user_list_file)

    for u in user_list:
        file = open(f"users\\{u.name}.txt", "rb")
        u.rated_items = pickle.load(file)
    if player.n_rated_items < 3:
        st.write("Por favor, avalie ao menos 3 itens para que possamos fazer recomendações baseadas em suas preferências")
    else:
        recommendations = recommend(player, user_list)
        for u in range(0, 5):
            st.write(recommendations[u][0])
