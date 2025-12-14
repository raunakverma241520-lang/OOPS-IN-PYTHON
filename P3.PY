class BankAccount:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
        
        
    def deposit(self, amount):
        self.balance +=amount
        
    def withdrawl(self, amount):
        self.balance -= amount
        
    def show_balance(self):
        print("Account Holder:",self.name)
        print("Balance:",self.balance)
        
b= BankAccount("Raunak Verma",5000)
b.deposit(1000)
b.withdrawl(1500)
b.show_balance()