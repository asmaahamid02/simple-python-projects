# #Banking App
# from datetime import datetime
 
# class Account:
#     def __init__(self) -> None:
#         self.balance = 0
#         self.owner = ""
#         self.transaction_list = []

#     def deposit(self, amount: float) -> None:
#         self.balance += amount
#         # (date): Deposited: {amount} - Balance: {self.balance}
#         transaction = f"{datetime.now()}: Deposited: {amount} - Balance: {self.balance}"
#         self.transaction_list.append(transaction)
#         print(f"Deposited: {amount} - Balance: {self.balance}")

#         # add the transaction to a file
#         with open(f"{self.owner}_transactions.txt", "a") as file:
#             file.write(transaction)

#     def withdraw(self, amount: float) -> None:
#         if self.balance >= amount:
#             self.balance -= amount
#             # (date): Withdrawn: {amount} - Balance: {self.balance}
#             transaction = f"{datetime.now()}: Withdrawn: {amount} - Balance: {self.balance}"
#             self.transaction_list.append(transaction)
#             print(f"Withdrawn: {amount} - Balance: {self.balance}")

#             # add the transaction to a file
#             with open(f"{self.owner}_transactions.txt", "a") as file:
#                 file.write(transaction)
#         else:
#             raise ValueError("Insufficient funds")

#     def show_balance(self) -> None:
#         print(f"Balance: {self.balance}")        

#     def show_transactions(self) -> None:
#         for index,transaction in enumerate(self.transaction_list):
#             print(f"{index+1}. {transaction}")

#     def __str__(self) -> str:
#         return f"Account Owner: {self.owner}\nAccount Balance: {self.balance}"
    

# def main():
#     account = Account()
#     account.owner = input("Enter your name: ")
#     while True:
#         print("1. Deposit")
#         print("2. Withdraw")
#         print("3. Show Balance")
#         print("4. Show Transactions")
#         print("5. Exit")
#         choice = int(input("Enter your choice: "))
#         if choice == 1:
#             amount = float(input("Enter the amount to deposit: "))
#             account.deposit(amount)
#         elif choice == 2:
#             amount = float(input("Enter the amount to withdraw: "))
#             account.withdraw(amount)
#         elif choice == 3:
#             account.show_balance()
#         elif choice == 4:
#             account.show_transactions()
#         elif choice == 5:
#             break
#         else:
#             print("Invalid choice")


# if __name__ == "__main__":
#     main()
from datetime import datetime

class Account:
    counter = 0

    def __init__(self, owner) -> None:
        Account.counter += 1
        self.id = Account.counter
        self.owner = owner
        self.balance = 0

    def _getTransaction(self, amount, type='deposit') -> str:
        if type == 'deposit':
            return f"({datetime.now()}): Deposited: ${amount} - Balance: ${self.balance}\n"
        return f"({datetime.now()}): Withdrawn: ${amount} - Balance: ${self.balance}\n"

    def _getFileName(self) -> str:
        return f"{self.owner.lower().strip().replace(" ","")}.txt"
    
    def _registerTransaction(self, transaction) -> str:
        filename = self._getFileName()
        with open(filename,"a") as file:
            file.write(transaction)
    
    def deposit(self, amount:float) -> None:
        try:
            amount = float(amount)
        except ValueError:
            amount = 0

        if amount > 0:           
            self.balance += amount

            transaction = self._getTransaction(amount)
            
            self._registerTransaction(transaction)

            print(f"${amount} deposited successfully. Balance: ${self.balance}\n")
        else:
            print("Invalid amount, could not process transaction. Try again\n")

    def withdraw(self, amount: float) -> None:
        try:
            amount = float(amount)
        except ValueError:
            amount = 0

        if amount > 0:
            if(self.balance >= amount):
                self.balance -= amount

                transaction = self._getTransaction(amount, 'withdraw')
                self._registerTransaction(transaction)

                print(f"${amount} withdrawn successfully. Balance: ${self.balance}\n")
            else:
                print("Insufficient funds, could not process transaction. Try again\n")
        else:
            print("Invalid amount, could not process transaction. Try again\n")        

    def showBalance(self) -> None:
        print(f"Balance: ${self.balance}\n")

    def showTransactions(self) -> None:
        with open(self._getFileName(), 'r') as file:
            for line in file:
                print(line)


def main() -> None:
    name = input("Enter your name: ").strip()

    account = Account(name)

    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show balance")
        print("4. Show transactions")
        print("5. Exit")

        try:
            choice = int(input("Choose an action: "))    

            if choice == 1:
                amount = input("Enter the amount to deposit: ")
                account.deposit(amount)
            elif choice == 2:
                amount = input("Enter the amount to withdraw: ")
                account.withdraw(amount)
            elif choice == 3:
                account.showBalance()
            elif choice == 4:
                account.showTransactions()        
            elif choice == 5:
                break        
            else:
                print("Please enter a valid choice")

        except ValueError:
            print("Invalid choice. Try again!")
            continue 
        except KeyboardInterrupt:
            print("\nLeaving ...\n")
            break   
        except Exception as error:
            print("Error ocurred: " , error)

if __name__ == "__main__":
    main()














