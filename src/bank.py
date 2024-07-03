from src.accounts import AccountBase, Savings_Account


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
