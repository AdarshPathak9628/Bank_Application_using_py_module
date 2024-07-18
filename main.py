from bank.Debtors import displayInfo  # Importing specific functions from Debtors
from bank.Depositor import  deposit,create_account, withdraw, enquiry, close  # Importing specific functions from Depositor
from bank.employee import *  # Importing specific function from employee

while True:
    print("\nMenu:")
    print("1. Enquiry")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Create Account")
    print("5. Display Information")
    print("6. Close Account")
    print("7. Exit")
    ch = int(input("Enter choice: "))  # Prompt user for choice
    
    if ch == 1:
        enquiry()  # Perform enquiry
    elif ch == 2:
        amt = int(input("Enter amount to withdraw: "))  # Prompt user for withdrawal amount
        withdraw(amt)  # Perform withdrawal with the specified amount
    elif ch == 3:
        amt = int(input("Enter amount to deposit: "))  # Prompt user for deposit amount
        deposit(amt)  # Perform deposit with the specified amount
    elif ch == 4:
        create_account()  # Create a new account
    elif ch == 5:
        displayInfo()  # Display account information
    elif ch == 6:
        close()  # Close an account
    elif ch == 7:
        break  # Exit the loop
    else:
        print("Invalid choice. Please try again.")  # Print error message for invalid input

print("Thank you for using our bank services!")  # Print farewell message
