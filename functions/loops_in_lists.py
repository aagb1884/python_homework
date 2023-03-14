# chickens = [
#   { "name": "Margaret", "age": 2, "eggs": 0 },
#   { "name": "Hetty", "age": 1, "eggs": 2 },
#   { "name": "Henrietta", "age": 3, "eggs": 1 },
#   { "name": "Audrey", "age": 2, "eggs": 0 },
#   { "name": "Mabel", "age": 5, "eggs": 1 },
# ]

# def find_chicken_by_name( list, chicken_name ):
#   for chicken in list:
#     if chicken["name"] == chicken_name:
#       return chicken
#     else:
#       return None
    
# print(find_chicken_by_name(chickens, "Mabel"))

# needs to be different to find anything beyond first dictionary in list

chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]

# def find_chicken_by_name( list, chicken_name ):
#     for chicken in list:
#         if chicken["name"] == chicken_name:
#             return chicken
    
#     return None
    
# print(find_chicken_by_name(chickens, "Mabel"))

# # return will loop if at base level

# def find_chicken_by_name(list, chicken_name):
#     found_chicken = None #not found chicken yet so assume this

#     for chicken in list:
#         if chicken["name"] == chicken_name #consider adding input to parameters if necessary
#             found_chicken = chicken

#     return found_chicken

users = [
  { "user_id": 1, "first_name": "Guido", "last_name": "van Rossum" },
  { "user_id": 2, "first_name": "Katherine", "last_name": "Johnson" },
  { "user_id": 3, "first_name": "Dorothy", "last_name": "Vaughan" },
  { "user_id": 4, "first_name": "Hen", "last_name": "Solo" },
  { "user_id": 5, "first_name": "Mary", "last_name": "Jackson" },
]
# Given a list of users, write a function to find a user by id. Test your function works with a specific id (e.g. 4)

# function looking for id in list of dictionaries
# we want a found userr, but do not have one to begin with
# we want to find them fro their id in a list of dictitonaries
# there are existing user ids and oones we will need to input
# calling the function will ask for a list and a value from that list


def find_id (list, input_user_id):
    found_user = None

    for user in list:
        if user["user_id"] == input_user_id:
            found_user = user

    return found_user

print(find_id(users, 4))
