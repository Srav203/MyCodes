# Superclass: BankAccount
class BankAccount:
    
    # Public data member
    account_number = None
    
    # Protected data member
    _balance = None
    
    # Private data member
    __password = None
    
    # Constructor
    def __init__(self, account_number, balance, password):
        self.account_number = account_number
        self._balance = balance
        self.__password = password
    
    def displayAccountNumber(self):
        print("Account Number:", self.account_number)
    
    def _displayBalance(self):
        print("Balance:", self._balance)
    
    def __displayPassword(self):
        print("Password:", self.__password)
    
    def accessPrivateMethod(self):
        self.__displayPassword()

# Subclass: SavingsAccount
class SavingsAccount(BankAccount):
    
    def __init__(self, account_number, balance, password):
        BankAccount.__init__(self, account_number, balance, password)
    
    def accessProtectedMethod(self):
        self._displayBalance()

# Driver code
# Creating object of SavingsAccount
account = SavingsAccount("1234567890", 1000.0, "secure123")
account.displayAccountNumber()
account.accessProtectedMethod()
account.accessPrivateMethod()
print("Accessing protected member directly:", account._balance)
# Trying to access private member directly (will cause an error if uncommented)
# print(account.__password)
