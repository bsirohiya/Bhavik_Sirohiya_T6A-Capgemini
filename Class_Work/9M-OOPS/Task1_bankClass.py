class Bank:
    balance = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        
        self.balance += amount
        print(f"{amount} added")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        if self.balance < amount:
            print("Insufficient balance")
            return

        self.balance -= amount
        print(f"{amount} deducted")

    def checkBalance(self):
        return self.balance

user1 = Bank("hehe", 10) 

print(user1.checkBalance()) 
user1.deposit(10)
print(user1.checkBalance()) 
user1.withdraw(5)
print(user1.checkBalance()) 

user1.withdraw(1000)


