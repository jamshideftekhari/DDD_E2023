from dataclasses import dataclass
from typing import Any


@dataclass
class AccountCreated:
    """
    Domain event representing the creation of a new account.
    """
    account_id: str
    account_holder: str
    initial_balance: float


# Example of an Aggregate (Account)
class Account:
    def __init__(self, account_id: str, account_holder: str, initial_balance: float):
        self.account_id = account_id
        self.account_holder = account_holder
        self.balance = initial_balance

        # Trigger the AccountCreated event when a new account is created
        account_created_event = AccountCreated(
            account_id=self.account_id,
            account_holder=self.account_holder,
            initial_balance=self.balance
        )

        # Handling the event (In a real application, you might publish it to an event bus)
        self.handle_account_created_event(account_created_event)

    def handle_account_created_event(self, event: AccountCreated):
        """
        Handle the AccountCreated event. In a real application, this method might publish
        the event to an event bus for further processing by other components.
        """
        print(f"Account {event.account_id} created for {event.account_holder} with an initial balance of {event.initial_balance}")


# Example of creating a new account
new_account = Account(account_id="123456", account_holder="John Doe", initial_balance=1000.0)
