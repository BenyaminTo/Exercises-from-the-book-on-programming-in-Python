class Account:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance
        if self.balance == -1:
            raise ValueError("Balance can not be -1!")
            self.balance = 0.0

    def credit(self, amount):
        if amount > 0:
            self.balance += amount 
            print(f"Deposit of {amount} successful. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def debit(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount 
                print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
            
    def getBalance(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance}"
#------------------------------------------------------------------------------
def menu():
    print("1. Credit\n2. Debit\n3. Get Balance\n Another out!\n")
    print("Enter a number from 1 to 3:")
    item = int(input("Enter a number:"))
    return item
#------------------------------------------------------------------------------
while(True):
    try:
        account_number = int(input("\nEnter account number:"))
        balance = float(input("Enter balance:"))  
        if balance == -1:
            raise ValueError("Balance can not be -1!")
    except ValueError as e:
        print(e)
        acc = Account(account_number, balance = 0.0)
        
    finally:
        action = menu()
        if action == 1:
            acc.credit(float(input("Enter amount:")))
        elif action == 2:
            acc.debit(float(input("Enter amount:")))
        elif action == 3:
            print(acc.getBalance())
        else:
           print("Out!")
           break

            