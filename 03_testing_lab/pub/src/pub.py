class Pub:
    
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def got_drink(self, drink):
        if drink in self.drinks:
            return True
       

    # def add_drink(self, drink):
    #     self.drinks.append(drink) 

    
            

    def sell_drink(self, drink, customer):
            if customer.age >=18 and customer.drunkenness < 50:
                    self.till += drink.price
                    customer.buy_drink(drink)
        # doesnt just increase till but also takes customer and 
        # uses 'customer.buy_drink'
        # one complicated function is harder to test
        # break down into smaller functions

    def check_age(self, customer):
        if customer.age >= 18:
            return True
        else: False
# don't need to return true or false here, implied