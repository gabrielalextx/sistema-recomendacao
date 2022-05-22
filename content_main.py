from content_item import CItem
import random
import pickle


def content_main():
    games = {
        'The Witcher 3': {'RPG': 4.5, 'Adventure': 5.0, 'Story Rich': 5.0, 'Open World': 5.0, 'Game Time': 5.0},
        'The Witcher 2': {'RPG': 4.0, 'Adventure': 4.5, 'Story Rich': 5.0, 'Open World': 4.0, 'Game Time': 3.0},
        'The Witcher 1': {'RPG': 4.0, 'Adventure': 4.0, 'Story Rich': 4.0, 'Open World': 3.0, 'Game Time': 4.0},
        'Elden Ring': {'RPG': 4.0, 'Action': 5.0, 'Multiplayer': 3.0, 'Open World': 5.0, 'Game Time': 4.0},
        'Detroit: Become Human': {'Action': 3.0, 'Adventure': 3.5, 'Story Rich': 5.0, 'Singleplayer': 5.0, 'Game Time': 2.0},
        'CS: GO': {'FPS': 5.0, 'Multiplayer': 5.0, 'Action': 5.0, 'Co-op': 3.0, 'Competitive': 5.0},
        'Valorant': {'FPS': 5.0, 'Multiplayer': 5.0, 'Action': 0.0, '?': 0.0, 'Competitive': 5.0},
        'COD: Modern Warfare': {'FPS': 5.0, 'Multiplayer': 4.0, 'Action': 5.0, 'Co-op': 2.0, 'Competitivo': 4.0},
        'Rainbow Six Siege': {'FPS': 4.0, 'Multiplayer': 5.0, 'Action': 5.0, 'Co-op': 1.0, 'Competitivo': 5.0},
        'Back 4 Blood': {'FPS': 3.5, 'Multiplayer': 4.5, 'Action': 5.0, 'Co-op': 4.5, 'Competitivo': 2.0},
        'Disco Elysium': {'RPG': 4.0, 'Indie': 4.0, 'Story Rich': 4.0, 'Open World': 3.5, 'Game Time': 2.5},
        'Dying Light 2 Stay Human': {'Survival': 4.0, 'Action': 3.5, 'Story Rich': 2.0, 'Open World': 3.0, 'Game Time': 3.5},
        'Red Dead Redemption 2': {'FPS': 2.0, 'Adventure': 4.0, 'Story Rich': 5.0, 'Open World': 5.0, 'Game Time': 5.0},
        'Metro Exodus': {'FPS': 3.5, 'Survival': 4.0, 'Story Rich': 4.5, 'Open World': 4.0, 'Game Time': 2.5},
        'The Elder Scrolls V: Skyrim': {'RPG': 4.5, 'Adventure': 5.0, 'Story Rich': 4.0, 'Open World': 4.0, 'Game Time': 3.5},
        'This War of Mine': {'RPG': 2.5, 'Indie': 4.0, 'Survival': 5.0, 'Adventure': 4.5, 'Game Time': 3.0},
        'Mass Effect: Legendary Edition': {'RPG': 4.0, 'Adventure': 4.0, 'Story Rich': 5.0, 'Singleplayer': 5.0, 'Game Time': 4.0},
        'Batman: Arkham Knight': {'Action': 4.0, 'Adventure': 4.0, 'Story Rich': 3.5, 'Open World': 4.5, 'Game Time': 2.5},
        'Baldurs Gate 3': {'RPG': 5.0, 'Adventure': 4.0, 'Story Rich': 3.5, 'Co-op': 2.5, 'Game Time': 3.0},
        'Barotrauma': {'Survival': 4.5, 'Multiplayer': 5.0, 'Co-op': 4.5, 'Action': 3.0, 'Horror': 3.5},
        'Project Zomboid': {'Survival': 5.0, 'Multiplayer': 3.5, 'Horror': 3.0, 'Open World': 4.0, 'Indie': 5.0},
        'STAR WARS Jedi Fallen Order': {'Adventure': 4.0, 'Action': 4.0, 'Story Rich': 4.5, 'Open World': 3.0, 'Game Time': 3.0},
        'Deathloop': {'FPS': 3.0, 'Action': 4.0, 'Multiplayer': 2.5, 'Adventure': 4.0, 'Game Time': 3.0},
        'Returnal': {'Roguelike': 4.5, 'Action': 4.0, 'Adventure': 3.0, 'Co-op': 2.5, 'Game Time': 3.5},
        'Hades': {'Roguelike': 5.0, 'Action': 4.0, 'Story Rich': 5.0, 'Adventure': 3.5, 'Game Time': 5.0},
        'Noita': {'Roguelike': 5.0, 'Indie': 5.0, 'Action': 3.0, 'Open World': 3.0, 'Game Time': 3.5},
        'Dead Cells': {'Roguelike': 5.0, 'Indie': 5.0, 'Action': 4.0, 'Singleplayer': 4.0, 'Game Time': 2.0},
        'The Last Of Us': {'Survival': 4.0, 'Adventure': 4.5, 'Story Rich': 5.0, 'Singleplayer': 5.0, 'Game Time': 2.0},
        'The Last Of Us Part 2': {'Survival': 4.0, 'Adventure': 4.5, 'Story Rich': 5.0, 'Singleplayer': 5.0, 'Game Time': 2.5},
        'Phasmophobia': {'Horror': 5.0, 'Co-op': 4.0, 'Multiplayer': 4.0, 'Indie': 3.5, 'Action': 1.0},
        'The Long Dark': {'Survival': 5.0, 'Open World': 3.0, 'Adventure': 3.5, 'Indie': 3.0, 'Game Time': 2.5},
        'Horizon: Zero Dawn': {'RPG': 3.5, 'Adventure': 4.5, 'Story Rich': 5.0, 'Open World': 4.5, 'Game Time': 3.5},
        'Portal 2': {'FPS': 2.0, 'Co-op': 2.5, 'Story Rich': 4.5, 'Strategy': 4.0, 'Game Time': 1.5},
        'The Legend of Zelda: Breath of the Wild': {'RPG': 2.5, 'Adventure': 4.0, 'Story Rich': 4.0, 'Open World': 4.5, 'Game Time': 3.5},
        'Resident Evil: Village': {'FPS': 3.0, 'Horror': 4.5, 'Story Rich': 4.5, 'Action': 3.5, 'Game Time': 2.0},
        'Little Nightmares 2': {'Horror': 5.0, 'Adventure': 3.5, 'Co-op': 2.0, 'Indie': 4.0, 'Game Time': 1.5},
        'Until Dawn': {'Horror': 5.0, 'Adventure': 4.0, 'Action': 2.0, 'Story Rich': 3.0, 'Game Time': 1.5},
        'Dead By Daylight': {'Horror': 5.0, 'Multiplayer': 4.0, 'Action': 2.0, 'Co-op': 4.0, 'Survival': 2.5},
        'DayZ': {'Survival': 5.0, 'Horror': 3.5, 'FPS': 2.5, 'Indie': 2.0, 'Multiplayer': 5.0},
        'Portal': {'FPS': 2.0, 'Singleplayer': 5.0, 'Story Rich': 4.0, 'Strategy': 4.0, 'Game Time': 1.0},
        'XCOM: Enemy Unknown': {'Strategy': 4.5, 'Multiplayer': 2.0, 'Singleplayer': 4.0, 'Action': 4.0, 'Game Time': 3.5},
        'XCOM 2': {'Strategy': 4.5, 'Multiplayer': 2.0, 'Singleplayer': 4.0, 'Action': 4.0, 'Game Time': 3.0},
        'Civilization VI': {'Strategy': 5.0, 'Multiplayer': 4.0, 'Co-op': 2.5, 'Singleplayer': 3.5, 'Action': 2.0},
        'Total War: Warhammer II': {'Strategy': 5.0, 'Action': 4.5, 'Multiplayer': 3.0, 'Co-op': 3.0, 'Game Time': 5.0},
        'Crusader Kings 3': {'Strategy': 5.0, 'RPG': 2.0, 'Singleplayer': 4.0, 'Multiplayer': 3.0, 'Game Time': 5.0},
        'Halo Infinite': {'FPS': 5.0, 'Multiplayer': 4.5, 'Competitivo': 4.0, 'Story Rich': 3.0, 'Game Time': 2.0},
        'It Takes Two': {'Co-op': 4.5, 'Story Rich': 5.0, 'Action': 4.0, 'Adventure': 4.0, 'Game Time': 2.0},
        'Apex Legends': {'FPS': 5.0, 'Multiplayer': 5.0, 'Action': 4.0, 'Co-op': 4.0, 'Competitivo': 4.5},
        'Destiny 2': {'FPS': 4.0, 'Multiplayer': 5.0, 'Co-op': 4.0, 'Open World': 3.0, 'Game Time': 5.0},
        'Dark Souls 3': {'RPG': 4.0, 'Action': 5.0, 'Multiplayer': 3.0, 'Open World': 5.0, 'Game Time': 2.5}
    }

    list_items = []
    for i in games.keys():
        x = CItem(i, games[i])
        list_items.append(x)

    print(list_items[0].categories)

    player_initial_recommendations = []
    while len(player_initial_recommendations) < 3:
        it = random.choice(list_items)
        if it not in player_initial_recommendations:
            player_initial_recommendations.append(it)

    print(player_initial_recommendations)

    file1 = open("list_items.txt", "wb")
    pickle.dump(list_items, file1)

    file3 = open("player_initial_recommendations.txt", "wb")
    pickle.dump(player_initial_recommendations, file3)


content_main()