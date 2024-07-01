from abc import ABC, abstractmethod
from datetime import datetime

class AccountBase(ABC):
    def __init__(self, owner: str, account_number: int, balance: int):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
        self._created = datetime.now()
        self._updates = None
    
    @abstractmethod
    def deposit(self, amount: int) -> None:
        self.balance += amount
        print(f"succesful withdrawed: {amount}")
        print(f"new balance = {self.balance}")

    def withdraw(self, amount: int) -> None:
        if self.balance >= amount:  
            self.balance -= amount
            self._created = datetime.now()
            print(f"succesful withdrawed: {amount}")
            print(f"new balance = {self.balance}")
        else:
            print("you ran out of money friend")

class Savings_Account(AccountBase):
    def __init__(self, name, account_number, balance, interest_rate):
        super().__init__(name, account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount: int):
        self.balance += amount
        print(f"succesfully raised your money with {amount}")
        print(f"new balance = {self.balance}")

    def add_interest(self):
        self.balance *= self.interest_rate
        print("your annual interest is added")
        print(f"your new balance = {self.balance}")
    
    def compound_interest_calculator(self, n_years):
        print(self.balance * (self.interest_rate  ** n_years))

    
  

