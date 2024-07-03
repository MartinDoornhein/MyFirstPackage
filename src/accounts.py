from abc import ABC, abstractmethod
from datetime import datetime

class AccountBase(ABC):
    def __init__(self, account_name: str, bank_name, balance: float = 0) -> None:
        
        """
        Initiliazation method for AccountBase Subclasses
        """
        
        self._account_name = account_name
        self._bank_name = bank_name
        self._created = datetime.now()
        self._updates = None
        self._balance = balance
    
    @abstractmethod
    def deposit(self, amount: int) -> None:
        pass


    def withdraw(self, amount: int) -> None:
        if self.balance >= amount:  
            self.balance -= amount
            self._created = datetime.now()
            print(f"succesful withdrawed: {amount}")
            print(f"new balance = {self.balance}")
        else:
            print("you ran out of money friend")

class Savings_Account(AccountBase):
    def __init__(self, name: str, balance: float, interest_rate: float = 1.05):
        super().__init__(name, balance)
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

    
class StudentAccount(AccountBase):
    pass

