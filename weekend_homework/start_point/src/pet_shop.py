# WRITE YOUR FUNCTIONS HERE

# 1
def get_pet_shop_name(name):
    return name["name"]

# 2

def get_total_cash(sum):
    return sum["admin"]["total_cash"]

# 3
# 4

def add_or_remove_cash(total, cash):
    total["admin"]["total_cash"] += cash
    

# 5

def get_pets_sold(sold):
    return sold["admin"]["pets_sold"]

# 6

# def increase_pets_sold(sold, int):
#     sold["admin"]["pets_sold"] = int
def increase_pets_sold(sold, int):
    sold["admin"]["pets_sold"] += int
# 7

def get_stock_count(count):
   return len(count["pets"])
      

# 8

def get_pets_by_breed(pet_shop,breed_of_pet):
    counter = 0
    pet = pet_shop["pets"]
    for pet in pet_shop:
        if pet["breed"] == breed_of_pet:
            counter += counter
            


# we need to get 2 instances of string "British Shorthair"
# these are in a dictionary in a list "pets"
# we need to loop through list matching key "breed"
# line 42 returns 'string indices must be integers'
# i don't know why


#  9

# 10

# def find_pet_by_name(pet_shop, name):
#     pets = pet_shop["pets"]
#     if name == search_name["name"]
        
          

# 11

def remove_pet_by_name(pet_shop, name):
    pet_shop = pet_shop["pets"]
    if pet_shop["name"] == name:
         pet_shop["name"].remove[name]

# def remove_friend(person, old_friend):
#   person["friends"].remove(old_friend)
# added this in from other work as reference

# 12
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop = pet_shop["pets"]
    pet_shop.append(new_pet)

# 13
# def get_customer_cash(cash):
#     for cash in customers:
#         if cash["cash"] == cash:
#             return cash
# consider returning list of customers whose cash equals that amount
# create empty list to append them into 
# turn list into string 

# 14

def remove_customer_cash(customer, amount):
    customer["cash"] = customer["cash"] - amount


# 15
def get_customer_pet_count(customer):
    return len(customer["pets"])
    
        #massively overthought this one as still have problems asserting values of dict in list in dict,
        # keep forgetting it's paremeter["key"]  

# 16

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    
#     def add_friend(person, new_friend):
#   person["friends"].append(new_friend)