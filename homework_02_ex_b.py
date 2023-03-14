users = {
    "Jonathan": {
        "twitter": "jonnyt",
        "lottery_numbers": [6, 12, 49, 33, 45, 20],
        "home_town": "Stirling",
        "pets": [
            {
              "name": "fluffy",
              "species": "cat"
            },
            {
              "name": "fido",
              "species": "dog"
            },
            {
              "name": "spike",
              "species": "dog"
            }
        ]
    },
    "Erik": {
        "twitter": "eriksf",
        "lottery_numbers": [18, 34, 8, 11, 24],
        "home_town": "Linlithgow",
        "pets": [
            {
              "name": "nemo",
              "species": "fish"
            },
            {
              "name": "kevin",
              "species": "fish"
            },
            {
              "name": "spike",
              "species": "dog"
            },
            {
              "name": "rupert",
              "species": "parrot"
            }
        ]
    },
    "Avril": {
        "twitter": "bridgpally",
        "lottery_numbers": [12, 14, 33, 38, 9, 25],
        "home_town": "Dunbar",
        "pets": [
            {
              "name": "monty",
              "species": "snake"
            }
        ]
    }
}
# dictionary inside list inside dictionary inside dictionary 
# look at brackets [] in blue indicate list

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)

print(users["Jonathan"]["twitter"])

# 2. Get Erik's hometown

print(users["Erik"]["home_town"])

# 3. Get the list of Erik's lottery numbers

print(users["Erik"]["lottery_numbers"])

# 4. Get the species of Avril's pet Monty

users["Avril"]["pets"][0]["species"]

# 5. Get the smallest of Erik's lottery numbers

sorted(users["Erik"]["lottery_numbers"])[0]
# sort list (min to max), use index number to identify smallest
# changes order of list

# THESE ALSO WORK
# smallest_number = min(users["Erik"]["lottery_numbers"])
# print("The smallest of Erik's lottery numbers is", smallest_number)
# min(users["Erik"]["lottery_numbers"]

# 6. Return an list of Avril's lottery numbers that are even

lottery_numbers = users["Avril"]["lottery_numbers"]
even_numbers = []
for lottery_number in lottery_numbers:
  if  lottery_number % 2 == 0:
      even_numbers.append(lottery_number)

print(even_numbers)

# lottery numbers gets a list
# create empty list to store even numbers so there's a place to store
# create for loop
# for lottery_number in users["Avril"]["lottery_numbers"]:
#     if lottery_number % 2 == 0:
#         print(users["Avril"]["lottery_numbers"]),

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers

# update(users["Erik"]["lottery_numbers"] = 7)

users["Erik"]["lottery_numbers"].append(7)

# 8. Change Erik's hometown to Edinburgh

users["Erik"]["home_town"] = "Edinburgh",
# print(users["Erik"])

# 9. Add a pet dog to Erik called "fluffy"

# pets is list, append dictionary to list
# square brackets for list, curly for dictionary
# so add curly brackets to square bracket elements

users["Erik"]["pets"].append({ "name": "Fluffy", "species": "dog" })


# new_pet = ["fluffy", "dog",]
# users.insert["Erik"]["pets"][new_pet]
# print(users["Erik"])
# this could have worked if i had an index number

# 10. Add another person to the users dictionary

users["ian"] = {
   "twitter": "twitterr name",
   "lottery_numbers": [4,5,6,7,8],
   "home_town": "Edinburgh",
   "pets": [
   {
      "name": "Dave",
      "species": "dog"
   }
   ]
}
# adding value to keys here
