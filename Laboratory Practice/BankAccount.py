from abc import ABC, abstractmethod

#1. Abstract class
class BankAccount(ABC):
    def __init__(self, account_number, balance = 0):
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

#2. CurrentAccount subclass
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

#3. SavingsAccount subclass
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
    print("Account Number:", account.account_number)
    print("Balance:", account.balance)
    print("Account Type:", account.display_account_type())
    print("-" * 40)

# Testing
if __name__ == "__main__":
    sa1 = SavingsAccount("SA001", 1000)
    sa2 = SavingsAccount("SA002", 500)
    ca1 = CurrentAccount("CA001", 2000)
    ca2 = CurrentAccount("CA002", -3000)

    sa1.deposit(200)
    sa1.withdraw(100)

    sa2.withdraw(600)
    sa2.deposit(400)

    ca1.withdraw(6500)
    ca1.deposit(1000)

    ca2.withdraw(3000)
    ca2.deposit(500)

    accounts = [sa1, sa2, ca1, ca2]
    for acc in accounts:
        print_account_details(acc)
