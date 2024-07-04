from abc import ABC, abstractmethod
from datetime import datetime


class AccountBase(ABC):
    def __init__(self, account_name: str, bank_name, balance: float) -> None:
        """
        Initiliazation method for AccountBase Subclasses
        """

        self._account_name = account_name
        self._bank_name = bank_name
        self._created = datetime.now()
        self._updates = None
        self.balance = balance

    @abstractmethod
    def deposit(self, amount: int) -> None:
        pass

    def withdraw(self, amount: int) -> None:
        if self.balance >= amount:
            self.balance -= amount
            self._created = datetime.now()
            return f"succesful withdrawed: {amount} \nnew balance = {self.balance} "
        else:
            return "you ran out of money friend"

    def info(self):
        return f"bank name: {self._bank_name}"
        # f"account_name: {self._account_name}")
        # print(f"created account on: {self._created}")
        # print(f"balance: {self.balance}")


class Savings_Account(AccountBase):
    def __init__(
        self,
        account_name: str,
        bank_name: str,
        balance: float = 0,
        interest_rate: float = 1.05,
    ):
        super().__init__(account_name, bank_name, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount: int):
        self.balance += amount
        return f"succesfully raised your money with {amount} \nnew balance = {self.balance}"

    def add_interest(self):
        self.balance *= self.interest_rate
        return f"your annual interest is added \nyour new balance = {self.balance}"

    def change_interest_rate(self, new_interest_rate: float):
        self.interest_rate = new_interest_rate
        return f"interest rate changed to {new_interest_rate}"

    def compound_interest_calculator(self, n_years):
        return self.balance * (self.interest_rate**n_years)


class StudentAccount(AccountBase):
    pass
