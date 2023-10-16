# Sample user account data (for demonstration purposes)
user_accounts = {
    "12345": {"pin": "6789", "balance": 1000.0},
    "54321": {"pin": "9876", "balance": 2000.0},
}

# Function to validate the user ID and PIN
def login():
    user_id = input("Enter your user ID: ")
    pin = input("Enter your PIN: ")

    if user_id in user_accounts and user_accounts[user_id]["pin"] == pin:
        print("Login successful! Welcome to the ATM.")
        return user_id
    else:
        print("Invalid user ID or PIN. Please try again.")
        return None

# Function to display the main menu
def main_menu():
    print("\nMain Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

# Function to check account balance
def check_balance(user_id):
    balance = user_accounts[user_id]["balance"]
    print(f"Your account balance is ${balance:.2f}")

# Function to deposit money
def deposit(user_id):
    amount = float(input("Enter the amount to deposit: $"))
    user_accounts[user_id]["balance"] += amount
    print(f"${amount:.2f} has been deposited into your account.")

# Function to withdraw money
def withdraw(user_id):
    amount = float(input("Enter the amount to withdraw: $"))
    if amount <= user_accounts[user_id]["balance"]:
        user_accounts[user_id]["balance"] -= amount
        print(f"${amount:.2f} has been withdrawn from your account.")
    else:
        print("Insufficient funds. Withdrawal not allowed.")

# Main program loop
while True:
    user_id = login()
    if user_id is not None:
        while True:
            main_menu()
            choice = input("Select an option (1/2/3/4): ")
            if choice == "1":
                check_balance(user_id)
            elif choice == "2":
                deposit(user_id)
            elif choice == "3":
                withdraw(user_id)
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                exit()
            else:
                print("Invalid option. Please try again.")
