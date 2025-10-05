# programming_paradigm/bank_account.py

class BankAccount: # A simple Bank Account class to demonstrate basic OOP concepts.

    def __init__(self, initial_balance=0.0): # Initialize account with an optional starting balance.
       
        self.__account_balance = float(initial_balance)

    def deposit(self, amount): # Add the specified amount to the account balance.
        
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account balance.
        Returns True if successful, False if insufficient funds.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True

    def display_balance(self): # Print the current account balance.
        
        print(f"Current Balance: ${self.__account_balance:.0f}")

# programming_paradigm/main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${int(amount)}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${int(amount)}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
