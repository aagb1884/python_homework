stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list

stops.append("Edinburgh Waverley")

#2. Add "Glasgow Queen St" to the start of the list

stops.insert(0, "Glasgow Queen St")

#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")

stops.insert(4, "Polmont")

#4. Print out the index position of "Linlithgow"

stops.index("Linlithgow")

item = "Linlithgow"
index = stops.index(item)
print('The index of', item, 'in the list is', index)

#5. Remove "Livingston" from the list using its name

stops.remove("Livingston")

#6. Delete "Cumbernauld" from the list by index

stops.pop(2)
# stops.pop(stops.index("Cumbernauld"))
# del stops[stops.index("Cumbernauld")] - this is so we know we're deleting Cumbernauld

#7. Print the number of stops there are in the list

number_stops = len(stops)
print('The number of stops on the list is', number_stops)
# len(stops)
# print(len(stops))

#8. Sort the list alphabetically

stops.sort()
# sorted(stops)

#9. Reverse the positions of the stops in the list

stops.reverse()

#10 Print out all the stops using a for loop

for stop in stops:
    print(stop)