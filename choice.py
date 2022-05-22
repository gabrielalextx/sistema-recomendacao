import streamlit as st
import pickle


def app():
    st.title("Escolha")
    st.write("Por favor, avalie cada um dos jogos com notas de 0 a 10:")

    player_recommendations_file = open("player_initial_recommendations.txt", "rb")
    player_initial_recommendations = pickle.load(player_recommendations_file)
    player_rating = [0, 0, 0]
    col1, col2, col3 = st.columns(3)

    with col1:
        item = player_initial_recommendations[0]
        st.write(item.name)
        rating = st.selectbox("Você gostou da recomendação?", ("Escolha", "Sim", "Não"), key=0)
        player_rating[0] = rating

    with col2:
        item = player_initial_recommendations[1]
        st.write(item.name)
        rating = st.selectbox("Você gostou da recomendação?", ("Escolha", "Sim", "Não"), key=1)
        player_rating[1] = rating

    with col3:
        item = player_initial_recommendations[2]
        st.write(item.name)
        rating = st.selectbox("Você gostou da recomendação?", ("Escolha", "Sim", "Não"), key=2)
        player_rating[2] = rating
    
    player_rating_file = open("player_rating.txt", "wb")
    pickle.dump(player_rating, player_rating_file)

    print(player_rating)