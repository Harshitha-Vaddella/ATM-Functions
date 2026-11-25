class BankAccount:

    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully!")
        else:
            print("Enter a valid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print("Amount withdrawn successfully!")

    def check_balance(self):
        print("Current Balance:", self.__balance)


class Transaction:

    def execute(self, account):
        pass


class Deposit(Transaction):

    def execute(self, account):
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)


class Withdraw(Transaction):

    def execute(self, account):
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)


class ATM:

    def __init__(self, account):
        self.account = account

    def menu(self):

        while True:
            print("\n----- ATM MENU -----")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                transaction = Deposit()
                transaction.execute(self.account)

            elif choice == '2':
                transaction = Withdraw()
                transaction.execute(self.account)

            elif choice == '3':
                self.account.check_balance()

            elif choice == '4':
                print("Thank you for using ATM!")
                break

            else:
                print("Invalid choice!")


account = BankAccount(1000)

atm = ATM(account)

atm.menu()