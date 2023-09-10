rivers = [
     {"name": "Nile", "length": 4157},
     {"name": "Yangtze", "length": 3434},
     {"name": "Murray-Darling", "length": 2310},
     {"name": "Volga", "length": 2290},
     {"name": "Mississippi", "length": 2540},
     {"name": "Amazon", "length": 3915}
]

# # In a for loop, print out each river's name!
# for river in rivers:
#     print(river["name"])

# # In another for loop, add up and print out the total length of all the rivers!
# total = 0
# for river in rivers:
#     total += river["length"]

# print(total)

# Extension
# Print out every river's name that begins with the letter M !
# The length of the rivers are in miles. Print out every river's length in kilometres! (1 mile is roughly 1.6 km)

# for river in rivers:
#     if river["name"].startswith("M"):
#         print(river["name"])

# for river in rivers:
#     length_km = river["length"] * 1.6
#     print(f"river[length: {length_km}km]")

#     # EXTENSIONS
# pin = 1234
# balance = 50000
# input_pin = input("Please enter your PIN number!")
# # Checking if input pin is correct
# if(pin == int(input_pin)):
# # Prompting user for withdraw or deposit
#     user_choice = input("Would you like to deposit or withdraw cash?")
#     if(user_choice == "withdraw"):
# # Prompting user for withdraw amount
#         amount = input("Please enter your chosen amount to withdraw")
# # Print out new balance after withdraw
#         balance -= int(amount)
#         print("Your new balance is " + str(balance))
#     if(user_choice == "deposit"):
# # Prompting user for deposit amount
#         amount = input("Please enter your chosen amount to deposit")
# # Print out new balance after withdraw
#         balance += int(amount)
#         print("Your new balance is " + str(balance))
# else:
#     print("Incorrect PIN! Please try again!")
