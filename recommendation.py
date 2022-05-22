import pickle

import streamlit as st
from pisson import c_computeNearestNeighbor

def app():
    st.title("Recomendações")
    st.subheader("Aqui estão suas recomendações:")

    player_initial_recommendation_file = open("player_initial_recommendations.txt", "rb")
    player_initial_recommendation = pickle.load(player_initial_recommendation_file)
    player_rating_file = open("player_rating.txt", "rb")
    player_rating = pickle.load(player_rating_file)
    list_items_file = open("list_items.txt", "rb")
    list_items = pickle.load(list_items_file)

    #print(player_initial_recommendation[0].categories)
    print(player_rating)

    player_distance = c_computeNearestNeighbor(player_initial_recommendation[0], list_items)
    #print(player_distance[0][1].name)

    player_recommendation = []
    for i in range(len(player_initial_recommendation)): 
        if player_rating[i] == 'Sim': 
            player_recommendation.append(c_computeNearestNeighbor(player_initial_recommendation[i], list_items))



    for i in range(len(player_recommendation)):
        st.write(f"Jogos similares a {player_recommendation[i][0][1].name}:")
        for j in range(3):
            print(player_recommendation[i][j+1][1].name)
            st.write(player_recommendation[i][j+1][1].name)
    
    

"""
    if player_initial_recommendation.n_rated_items < 3:
        st.write("Por favor, avalie ao menos 3 itens para que possamos fazer recomendações baseadas em suas preferências")
    else:
        recommendations = recommend(player_initial_recommendation, user_list)
        for u in range(0, 5):
            st.write(recommendations[u][0])
"""
