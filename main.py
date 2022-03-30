import random
import pickle
import item as item
import user as user


def main():
    category = ['RPG', 'FPS', 'Adventure', 'Strategy', 'Roguelike', 'Survival', 'Horror']
    games = {
        1: ['The Witcher 3', 'RPG'],
        2: ['The Witcher 2', 'RPG'],
        3: ['The Witcher 1', 'RPG'],
        4: ['Elden Ring', 'RPG'],
        5: ['Detroit: Become Human', 'RPG'],
        6: ['CS: GO', 'FPS'],
        7: ['Valorant', 'FPS'],
        8: ['COD: Warzone', 'FPS'],
        9: ['Rainbow Six Siege', 'FPS'],
        10: ['Back 4 Blood', 'FPS'],
        11: ['Disco Elysium', 'RPG'],
        12: ['Dying Light 2 Stay Human', 'FPS'],
        13: ['Red Dead Redemption 2', 'Adventure'],
        14: ['Metro Exodus', 'Horror'],
        15: ['The Elder Scrolls V: Skyrim', 'Adventure'],
        16: ['This War of Mine', 'Survival'],
        17: ['Mass Effect: Legendary Edition', 'RPG'],
        18: ['Batman: Arkham Origins', 'Adventure'],
        19: ['Baldurs Gate 3', 'RPG'],
        20: ['Barotrauma', 'Strategy'],
        21: ['Project Zomboid', 'Strategy'],
        22: ['STAR WARS Jedi Fallen Order', 'RPG'],
        23: ['Deathloop', 'FPS'],
        24: ['Returnal', 'Roguelike'],
        25: ['Hades', 'Roguelike'],
        26: ['Noita', 'Roguelike'],
        27: ['Dead Cells', 'Roguelike'],
        28: ['The Last Of Us', 'Survival'],
        29: ['The Last Of Us 2', 'Survival'],
        30: ['Phasmophobia', 'Horror'],
        31: ['The Long Dark', 'Survival'],
        32: ['Horizon: Zero Dawn', 'Adventure'],
        33: ['Portal', 'Strategy'],
        34: ['The Legend of Zelda: Breath of the Wild', "Adventure"],
        35: ['Resident Evil: Village', 'Horror'],
        36: ['Little Nightmares 2', 'Horror'],
        37: ['Until Dawn', 'Horror'],
        38: ['Dead By Daylight', 'Horror'],
        39: ['DayZ', 'Horror'],
        40: ['Slay the Spire', 'Roguelike'],
        41: ['The Binding of Isaac', 'Roguelike'],
        42: ['XCOM 2', 'Strategy'],
        43: ['Civilization VI', 'Strategy'],
        44: ['Total War: Warhammer', 'Strategy'],
        45: ['Crusader King 3', 'Strategy'],
        46: ['Halo Infinite', 'FPS'],
        47: ['It Takes Two', 'Adventure'],
        48: ['Apex Legends', 'FPS'],
        49: ['Destiny 2', 'FPS'],
        50: ['Dark Souls 3', 'RPG']
    }

    n_users = 100

    n_items = 50
    list_items = []
    for i in games.keys():
        x = item.Item(games[i][0], games[i][1])
        list_items.append(x)

    list_users = []

    for i in range(n_users):
        x = user.User("user_%s" % str(i + 1))
        list_users.append(x)

    for u in list_users:
        for i in category:
            u.set_category_taste(i, random.uniform(0.5, 2))

    for u in list_users:
        for i in range(len(list_items)):
            if not 0:
                u.set_rating(list_items[i].name, list_items[i].category, random.randint(0, 10))

    player_initial_recommendations = []
    while len(player_initial_recommendations) < 3:
        it = random.choice(list_items)
        if it not in player_initial_recommendations:
            player_initial_recommendations.append(it)

    player = user.User("User")
    for i in category:
        player.set_category_taste(i, 1)

    print(list_users[0].name)
    print(list_users[0].rated_items)

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



