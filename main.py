import random
import item
import user
from pisson import recommend


def main():
    n_users = 10

    n_items = 50
    list_items = []
    for i in range(n_items):
        x = item.Item("item " + str(i+1), random.randint(1, 5))
        list_items.append(x)

    list_users = []

    for i in range(n_users):
        x = user.User("user %s" %str(i+1))
        list_users.append(x)

    for u in list_users:
        for i in range(1, 6):
            u.set_category_taste(i, random.uniform(0.5, 1.5))

    for u in list_users:
        for i in range(n_items):
            if not random.randint(0, 1):
                u.set_rating(list_items[i].name, list_items[i].category, random.randint(0, 10))

    print(recommend(list_users[0], list_users))
    print(list_users[0])
    '''while player.n_rated_items < 3:
        it = random.choice(list_items)
        if player.rated_items[it.name] is None:
            rating = int(input(f"rate {it.name}: "))
            player.set_rating(it.name, rating)'''


main()