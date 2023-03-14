# united_kingdom = [
#     {
#         "name": "Scotland",
#         "population": 5295000,
#         "capital": "Edinburgh"
#     },
#     {
#         "name": "Wales",
#         "population": 3063000,
#         "capital": "Swansea"
#     },
#     {
#         "name": "England",
#         "population": 53010000,
#         "capital": "London"
#     }
# ]

# # 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.

# united_kingdom[1]["capital"] = "Cardiff"

# # 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).

# united_kingdom.append({
#     "name": "Northern Ireland",
#     "population": 1811000,
#     "capital": "Belfast"
# })

# # 3. Use a loop to print the names of all the countries in the UK.

# for country in united_kingdom:
#     print(country["name"])

# # 4. Use a loop to find the total population of the UK.

# total_population = 0

# for country in united_kingdom:
#         total_population += country["population"]

# print(total_population)

# print(united_kingdom)

# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

even_numbers = []
for number in numbers:
    if number %2 == 0:
            even_numbers.append(number)

print(even_numbers)


# 2. Print the difference between the largest and smallest value:

largest = max(numbers)
smallest = min(numbers)

print(largest - smallest)

# 3. Print True if the list contains a 2 next to a 2 somewhere.

result = False
index = 1
for number in numbers:
    if (number ==1 and numbers [index-1] ==2):
         result = True
    index +=1
print(result)

# declare variable, set to false
# index refers to index position in list

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

total = 0
found_6 = False
for number in numbers:
        if number == 6:
              found_6 = True
        elif found_6:
              if number == 7:
                    found_6 = False
        else:
              total += number 

print(total)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 




