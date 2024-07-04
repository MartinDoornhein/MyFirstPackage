from src.accounts import AccountBase, Savings_Account
import pandas as pd


class Bank:
    def __init__(self, bank_name: str):
        self._name = bank_name
        self._accounts: list[AccountBase] = []

    def create_savings_account(
        self, account_name: str, initial_deposit: float
    ) -> AccountBase:
        s_account = Savings_Account(
            account_name=account_name, bank_name=self._name, balance=initial_deposit
        )
        self._accounts.append(s_account)

        print(
            f"succesfully created Savingscount with initial balance: {initial_deposit}"
        )
        return s_account

    def list_accounts(self) -> list[AccountBase]:
        """
        return list of accounts in Bank
        """

        return self._accounts

    def export_bank_accounts(self):
        account_dict = {}
        for account in self.list_accounts():
            # Create a dictionary for the current account's details
            account_details = {
                "bank_name": self._name,
                "account_name": account._account_name,
                "balance": account.balance,
                "interest_rate": account.interest_rate,
                "created": str(account._created),
            }

            # Use the account's name or some unique identifier as the key
            # and the account details dictionary as the value
            account_dict[account._account_name] = account_details
        return pd.DataFrame(account_dict)
