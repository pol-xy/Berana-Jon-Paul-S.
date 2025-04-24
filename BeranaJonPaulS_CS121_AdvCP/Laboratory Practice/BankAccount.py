from abc import ABC, abstractmethod

#1. Abstract base class
class BankAccount(ABC):
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    def _update_balance(self, new_balance):
        self.__balance = new_balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def display_account_type(self):
        pass

#2. Current account with overdraft
class CurrentAccount(BankAccount):
    overdraft_limit = -5000

    def deposit(self, amount):
        if amount > 0:
            self._update_balance(self.balance + amount)
            print(f"Deposited {amount} to Current Account {self.account_number}")
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount):
        if self.balance - amount >= self.overdraft_limit:
            self._update_balance(self.balance - amount)
            print(f"Withdrew {amount} from Current Account {self.account_number}")
        else:
            print("Overdraft limit exceeded!")

    def display_account_type(self):
        return "Current Account"

#3. Savings account without overdraft
class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self._update_balance(self.balance + amount)
            print(f"Deposited {amount} to Savings Account {self.account_number}")
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self._update_balance(self.balance - amount)
            print(f"Withdrew {amount} from Savings Account {self.account_number}")
        else:
            print("Insufficient balance!")

    def display_account_type(self):
        return "Savings Account"

#4. Polymorphic function
def print_account_details(account):
    print(f"Account Number: {account.account_number}")
    print(f"Balance: {account.balance}")
    print(f"Account Type: {account.display_account_type()}")
    print("-" * 40)

# Testing the system
if __name__ == "__main__":
    # Create accounts
    sa1 = SavingsAccount("SA001", 1000)
    sa2 = SavingsAccount("SA002", 500)
    ca1 = CurrentAccount("CA001", 2000)
    ca2 = CurrentAccount("CA002", -3000)

    # Perform operations
    sa1.deposit(200)         # New balance: 1200
    sa1.withdraw(100)        # New balance: 1100

    sa2.withdraw(600)        # Should fail
    sa2.deposit(400)         # New balance: 900

    ca1.withdraw(6500)       # Within overdraft (-4500)
    ca1.deposit(1000)        # New balance: -3500

    ca2.withdraw(3000)       # Should fail (would be -6000)
    ca2.deposit(500)         # New balance: -2500

    # Display all account details
    for account in [sa1, sa2, ca1, ca2]:
        print_account_details(account)
