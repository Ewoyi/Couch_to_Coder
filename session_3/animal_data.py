animals = [
     {"name": "capybara", "group": "mammal", "weight": 110},
     {"name": "hedgehog", "group": "mammal", "weight": 0.5},
     {"name": "bearded dragon", "group": "reptile", "weight": 1},
     {"name": "tortoise", "group": "reptile", "weight": 40},
     {"name": "hummingbird", "group": "bird", "weight": 0.01},
     {"name": "elephant", "group": "mammal", "weight": 10000},
     {"name": "ostrich", "group": "bird", "weight": 280},
     {"name": "python", "group": "reptile", "weight": 180},
     {"name": "blue whale", "group": "mammal", "weight": 300000},
     {"name": "lion", "group": "mammal", "weight": 350}
]


# 1. Print out all the animals names that are heavier than 100 pounds! 2. Print out the heaviest animal!
# 3. Print out the lightest/heaviest animal!
# 4. Print out all mammals as a list!

# Task 1

# Pseudocode

# loop through all the animal dicts inside the animal list
# check if the animal is has a weight greater than 100
# if it does, print out the name of the animal

# for animal in animals:
#     if animal["weight"] > 100:
#         print(animal["name"])


# Task 2

# Pseudocode

# Loop through all animal weights in the animal list
# find out which animal has the heighest weight value
# Compare animals weight to each other
# display the animal with the highest vale

# heaviest_animal = animals[0]

# for animal in animals:
#     if(animal["weight"] > heaviest_animal["weight"]):
#         heaviest_animal = animal
# print(heaviest_animal)

# lightest_animal = animals[0]

# for animal in animals:
#     if(animal["weight"] < lightest_animal["weight"]):
#         lightest_animal = animal
# print(lightest_animal)


# Task 3

# Pseudocode

# mammals = []

# for animal in animals:
#     if(animal["group"] == "mammal"):
#         mammals.append(animal)
# print(mammals)

# Task 4
# Print all animals with names larger than 7 letters

# Pseudocode

# Loop through all the mammals names in the list
# find out what animal with 7 letter names
# Display animals with 7 letter names


# for animal in animals:
#     if(len(animal["name"]) > 7):
#         print(animal["name"])


# Task 5
# print mammals with names larger than 7 letters

# Pseudocode

# Loop through all the mammals names in the list
# find out what animal with 7 letter names
# Display animals with 7 letter names

# mammals = []

# for animal in animals:
#     if(animal["group"] == "mammal"):
#         if(len(animal["name"]) > 7):
#             mammals.append(animal)
# print(mammals)
