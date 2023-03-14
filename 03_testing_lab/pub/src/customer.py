class Customer:
    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness

    def buy_drink(self, drink):
        self.wallet -= drink.price
        self.drunkenness += drink.alcohol_level

    def buy_food(self,food):
        self.wallet -= food.price
        self.drunkenness -= food.rejuvenation_level

# second simplest, does stuff, takes in drink object