import streamlit as st
import random
import pickle
import apps.item as item
import apps.user as user
from apps.pisson import recommend


def main():
    n_users = 10

    n_items = 50
    list_items = []
    for i in range(n_items):
        x = item.Item("item " + str(i+1), random.randint(1, 5))
        list_items.append(x)

    list_users = []

    for i in range(n_users):
        x = user.User("user_%s" %str(i+1))
        list_users.append(x)

    for u in list_users:
        for i in range(1, 6):
            u.set_category_taste(i, random.uniform(0.5, 1.5))

    for u in list_users:
        for i in range(n_items):
            if not 0:
                u.set_rating(list_items[i].name, list_items[i].category, random.randint(0, 10))

    player_initial_recommendations = []
    while len(player_initial_recommendations) < 3:
        it = random.choice(list_items)
        if it not in player_initial_recommendations:
            player_initial_recommendations.append(it)

    player = user.User("User")
    for i in range(1, 6):
        player.set_category_taste(i, 1)


    file1 = open("list_items.txt", "wb")
    pickle.dump(list_items, file1)

    for u in list_users:
        file = open(f"users\\{u.name}.txt", "wb")
        pickle.dump(u.rated_items, file)

    file2 = open("list_users.txt", "wb")
    pickle.dump(list_users, file2)
    file3 = open("player_initial_recommendations.txt", "wb")
    pickle.dump(player_initial_recommendations, file3)
    file4 = open("player.txt", "wb")
    pickle.dump(player, file4)

main()



