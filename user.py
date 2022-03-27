class User:
    name = ""
    n_rated_items = 0
    category_tastes = {}

    def __init__(self, name):
        self.name = name
        self.rated_items = {}

    def __str__(self):

        return "User %s Rated Items: %s\n%s" % (self.name ,self.n_rated_items, self.rated_items)

    def set_rating(self, item_name, item_category, points):
        if item_name not in self.rated_items.keys():
            self.n_rated_items += 1
        x = points * self.category_tastes[item_category]
        if x > 10:
            x = 10
        if x < 0:
            x = 0
        self.rated_items[item_name] = round(x)

    def get_rating(self, item_name):
        return self.rated_items[item_name]

    def set_category_taste(self, category, taste):
        self.category_tastes[category] = taste


