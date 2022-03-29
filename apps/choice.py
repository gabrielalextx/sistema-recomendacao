import streamlit as st
import pickle


def app():
    st.title("Escolha")
    st.write("Por favor, avalie cada um dos jogos com notas de 0 a 10:")

    player_file = open("apps\\player.txt", "rb")
    player_recommendations_file = open("apps\\player_initial_recommendations.txt", "rb")
    player_initial_recommendations = pickle.load(player_recommendations_file)
    player = pickle.load(player_file)
    col1, col2, col3 = st.columns(3)

    with col1:
        item = player_initial_recommendations[0]
        st.write(item.name)
        rating = st.number_input("Avalie de 0 a 10:", min_value=0, max_value=10, value=player.get_rating(item.name), key=1)
        player.set_rating(item.name, item.category, int(rating))

    with col2:
        item = player_initial_recommendations[1]
        st.write(item.name)
        rating = st.number_input("Avalie de 0 a 10:", min_value=0, max_value=10, value=player.get_rating(item.name), key=2)
        player.set_rating(item.name, item.category, int(rating))

    with col3:
        item = player_initial_recommendations[2]
        st.write(item.name)
        rating = st.number_input("Avalie de 0 a 10:", min_value=0, max_value=10, value=player.get_rating(item.name), key=3)
        player.set_rating(item.name, item.category, int(rating))

    player_file = open("apps\\player.txt", "wb")
    pickle.dump(player, player_file)
