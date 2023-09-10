# Pseudo code

# Create a file called control_flow_atm.py
# Create a variable called balance with an int value representing the money in the user's account
# Create a variable called pin with an int value (for example 1234)
# Prompt the user to enter their pin !
# If the pin values match, display their balance.
# If they don't match, print out a message notifying the user
# Extensions:
# If the pin matches, give the prompt to the user if they'd like to withdraw or deposit some money.
# Once they made their choice, prompt them to enter an amount.
# Subtract or add the value to their account balance, then display the updated balance!


# Create a file called control_flow_atm.py

# Create a variable called balance with an int value representing the money in the user's account
balance = 10000  

# Create a variable called pin with an int value (for example 1234)
pin = 1234  

# Prompt the user to enter their pin
user_pin = int(input("Enter your PIN"))

# If the pin values match, give the prompt to the user if they'd like to withdraw or deposit money.
if user_pin == pin:
    print("Welcome to the ATM!")
    print("1. Withdraw")
    print("2. Deposit")
    
    choice = int(input("Please choose an option (1/2)"))
    
    # If the user chooses to withdraw
    if choice == 1:
        amount = float(input("Enter the amount to withdraw"))
        if amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            print(f"Withdrawal successful. Your updated balance is: ${balance}")
    
    # If the user chooses to deposit
    elif choice == 2:
        amount = float(input("Enter the amount to deposit"))
        balance += amount
        print(f"Deposit successful. Your updated balance is ${balance}")
    
    else:
        print("Invalid choice")
    
else:
    print("Incorrect PIN. Please try again.")