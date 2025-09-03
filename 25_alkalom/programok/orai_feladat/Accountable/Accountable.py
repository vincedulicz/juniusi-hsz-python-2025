from abc import ABC, abstractmethod


class Accountable(ABC):
    """
    Abstract base class to define the interface for banking operations.
    """

    @abstractmethod
    def create_account(self, account_number: str, initial_balance: float = 0) -> None:
        """
        Create a new bank account.
        """
        pass

    @abstractmethod
    def make_deposit(self, account_number: str, amount: float) -> None:
        """
        Deposit money into an account.
        """
        pass

    @abstractmethod
    def make_withdrawal(self, account_number: str, amount: float) -> None:
        """
        Withdraw money from an account.
        """
        pass

    @abstractmethod
    def check_balance(self, account_number: str) -> None:
        """
        Check the balance of an account.
        """
        pass