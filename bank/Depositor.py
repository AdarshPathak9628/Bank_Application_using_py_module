bal = 50000  # Initial balance
emp = []  # List to store account information


def deposit():
    global bal
    a = float(input("Enter amount to deposit: "))  # Prompt for deposit amount
    bal += a  # Update the balance
    print("Your current balance: ", bal)  # Print updated balance

def create_account():
    global emp
    eid = int(input("Enter creator ID: "))  # Prompt for creator ID
    name = input("Enter the name: ")  # Prompt for account holder's name
    age = int(input("Enter the age: "))  # Prompt for account holder's age
    blc = 50000  # Initial balance for new account
    ap = [eid, name, age, blc]  # Create account details list
    emp.append(ap)  # Add account details to the list
    print(emp)  # Print the list of accounts (for demonstration)
    print("Your account has been opened successfully.")


def withdraw():
    global bal
    x = float(input("Enter amount to withdraw: "))  # Prompt for withdrawal amount
    if x <= bal:
        bal -= x  # Deduct withdrawal amount from balance if sufficient funds
        print("Your current balance: ", bal)  # Print updated balance
    else:
        print("Insufficient balance: ", x)  # Print error message if balance is insufficient

def enquiry():
    global bal
    print("Your current balance is: ", bal)  # Display current balance

def close():
    print("Your account has been closed successfully.")  # Display account closure message

#  Sample usage of functions
# create_account()   Example: Create an account
# deposit()     Example: Deposit money
# withdraw()    Example: Withdraw money
# enquiry()    Example: Check balance
# close()    Example: Close account
