class BankAccount:
    def __init__(self, account_number: str, balance: float):
        self.account_number = account_number
        self.balance = balance
    
    
    def deposit(self, amount):
        print(f"The money {amount} was added to your account")
        return self.balance + amount
    
    def withdraw(self, amount):
        if self.balance != 0:
            print(f"The money {amount} was withdraw from you account")
            return self.balance - amount
        else:
            print("Your bank account is empty")
    
    
    def get_balance(self):
        return self.balance
    

your_acc = BankAccount('890909887878', 670.67)
print(your_acc.deposit(67.9))
print(your_acc.withdraw(45.9))
print(your_acc.get_balance())