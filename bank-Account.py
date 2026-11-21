class BankAccount:
    def __init__(self,account_no,account_type,name,balance):
        self.account_no = account_no
        self.account_type = account_type
        self.name = name
        self.balance = balance

    # function for depositing amount
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print("Amount Deposited Successfully")
            print("Current Balance:",self.balance)
        else:
            print("Invalid Amount")

    # function for withdrawing amount
    def withdraw(self,amount):
        if amount < 0:
            print("Invalid Amount")
        elif amount<= self.balance:
            self.balance -= amount
            print("Amount Withdrad Successfully")
            print("Current Balance:", self.balance)
        else:
            print("Insufficient Balance")

    def display(self):
        print("\n----------Account Details---------")
        print("Account Holder:", self.name)
        print("Account No:",self.account_no)
        print("Account Type:",self.account_type)
        print("Balance:",self.balance)



account = BankAccount(223452617322,"Savings","Shadilal K.S",10000)
account.display()
print("----------------------------------")
account.deposit(10000)
print("----------------------------------")
account.withdraw(5000)
print("----------------------------------")