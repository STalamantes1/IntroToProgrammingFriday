# #How to make a list 
# favgames=["Halo","Elden Ring", "RE2", "RE2"]

# #Indexing a list 
# #Searching through a list via its placement 
# # print(favgames[0]) #This prints out the first list item 
# # print(favgames[1])
# # print(favgames[2])

# #Using Len() with a list 
# #We can use Len() to count how many items are in a list 
# # print(len(favgames))

# #Adding items to a list 
# #append() adds to the end of the list 
# #inser() adds an item to a specific position 

# favgames.append("Mario Kart")
# # print(len(favgames))

# #Inserting a list item at a certain position 
# favgames.insert(0,"RE4")
# # print(favgames)

# #Common List Methods 
# #Count() counts how many times a value appears
# #Remove() removes a specific item
# #Sort(), puts the list in a sorted order
# #Reverse(), flips the current order of the list 

# #Count() example
# print(favgames.count("RE2"))

# #Remove example 
# favgames.remove("RE2")
# # print(favgames)

# #Sort() example 
# favgames.sort()
# print(favgames)

# #Reverse() example 
# favgames.reverse()
# print(favgames)


# #Looping through a list 
# #We use a FOR loop when we want to print out the items in a list 

# for game in favgames:
#     print(game)



#Dictionaries 
#Dictionaries are usually accessed by key, not position 
#use a dictionary when labels matter and you want to look things up by name 

player_stats={
    #"Key": Value
    "Health":100,
    "Mana":40,
    "Level":7,
    "Gold":250
}
#A dictionary stores data in key-value pairs

#How to access data from a dictionary? 
print(player_stats["Health"])



#Adding and updating dictionary Values 
#You can add a new key-value pair by assigning a value to a new key
#We can also update an exisiting value or increase it 

#Adding a new Key:Value 
player_stats["Strength"]=12


#Update a value
player_stats["Health"]=250


#Adding to a value 
player_stats["Gold"]+=50


player_stats["Mana"]+=50
# print(player_stats)

#Keys() and Values()
#Keys() shows all dictionary keys
#Values() shows all dictionary values 

# print(player_stats.keys())
# print(player_stats.values())

#Looping through Dictionaries 
#You can loop through keys, values, or both 
# .items() is often the most readable way to show everything in a dictionary 
 
 #Key for loop 
# for key in player_stats.keys():
#     print(key)
# #Value FOR loop 
# for value in player_stats.values():
#     print(value)

# for key, value in player_stats.items():
#     print(f"{key}:{value}")


#Nested Dicitonaries 
students={
    "001":{
        "Name":"Ana",
        "Major":"Cyber",
        "credits":15,
        "HS Info":{
            "GPA":3.5
        }
    },
    "002":{
        "name":"Sebastian",
        "Major":"Networking",
        "Credits":15
    }

}
#Accessing Nested Dictionary Info 
#To access nested data, go one level at a time 
print(students["001"]["HS Info"]["GPA"])

#Combining a nested dictionary with a list 
cars={
    "Honda":{
        "Location":"Japan",
        "Founded":1950,
        "Models": ["NSX","Civic","Rebel","Accord"]
    }
}
print(cars["Honda"]["Models"])


