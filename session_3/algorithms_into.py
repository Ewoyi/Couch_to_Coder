# BASE TASK
# Setting up pin, balance, and number of tries
pin = 1234
balance = 50000
number_of_tries = 3
# prompting user for input
input_pin = input("Please enter your PIN number!")
# Given the number of tries 
while(number_of_tries > 0):
    if(not input_pin.isdigit()):
        print("Invalid Input, Please Try Again")
        break
# turning input to int() so it can check for equality between 2 ints
    if(pin == int(input_pin)):
# turning balance to str so we can combine with message
        print("Your balance is " + str(balance))
        break # Exit the loop when the pin is found
    else:
        number_of_tries -= 1
        # guard close
        if(number_of_tries == 0):
            break
        input_pin = input("Incorrect PIN! Please try again!")



