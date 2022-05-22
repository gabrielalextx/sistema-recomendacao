from user import User
from math import sqrt
from content_item import CItem

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }



def manhattan(rating1, rating2):
    """Computes the Manhattan distance. Both rating1 and rating2 are dictionaries
       of the form {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}"""
    distance = 0
    total = 0
    for key in rating1.keys():
        if key in rating2.keys():
            distance += abs(rating1[key] - rating2[key])
            total += 1
    if total > 0:
        return distance / total
    else:
        return -1 #Indicates no ratings in common



def pearson(rating1, rating2):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    for key in rating1:
        if key in rating2:
            n += 1
            x = rating1[key]
            y = rating2[key]
            sum_xy += x * y
            sum_x += x
            sum_y += y
            sum_x2 += pow(x, 2)
            sum_y2 += pow(y, 2)
    # now compute denominator
    denominator = sqrt(sum_x2 - pow(sum_x, 2) / n) * sqrt(sum_y2 - pow(sum_y, 2) / n)
    if denominator == 0:
        return 0
    else:
        return (sum_xy - (sum_x * sum_y) / n) / denominator
            

def computeNearestNeighbor(username, user_list):
    """creates a sorted list of users based on their distance to username"""
    distances = []
    for user in user_list:
        if user != username:
            distance = pearson(user.rated_items, username.rated_items)
            #print(distance)
            distances.append((distance, user))
    # sort based on distance -- closest first
    sorted(distances, key=lambda x: x[0])
    return distances


def c_computeNearestNeighbor(item, item_list):
    """creates a sorted list of users based on their distance to username"""
    distances = []
    for i in item_list:
        if i != item:
            distance = manhattan(item.categories, i.categories)
            distances.append((distance, i))
    # sort based on distance -- closest first
    sorted_distances = sorted(distances, key=lambda x: x[0])
    return sorted_distances

def recommend(username, user_list):
    """Give list of recommendations"""
    # first find nearest neighbor
    nearest = computeNearestNeighbor(username, user_list)[0][1]
    recommendations = []
    # now find bands neighbor rated that user didn't
    neighborRatings = nearest.rated_items
    userRatings = username.rated_items
    for item in neighborRatings.keys():
        if item not in userRatings.keys():
            recommendations.append((item, neighborRatings[item]))

    # using the fn sorted for variety - sort is more efficient
    return sorted(recommendations, key=lambda x: x[1], reverse = True)

