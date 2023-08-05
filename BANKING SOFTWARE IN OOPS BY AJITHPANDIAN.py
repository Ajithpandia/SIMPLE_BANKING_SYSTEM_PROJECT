class BankAccount:
    def _init_(self):
        self.name = ""
        self.pin = ""
        self.balance = 0.0

    def open_account(self):
        self.name = input("Enter customer name: ")
        self.pin = input("Enter PIN number: ")
        self.balance = float(input("Enter opening balance: "))
        print(f"Hi! {self.name} your Account was successfully created.")
        print(f"Thank you {self.name} for choosing TIMES BANK")

    def deposit(self):
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            self.balance += amount
            print(f"Hi!{self.name} your amount {amount} was successfully deposited into your account.")
        else:
            print("Invalid amount. Deposit failed.")

    def withdraw(self):
        amount = float(input("Enter withdrawal amount: "))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Hi {self.name}, Your Amount {amount} Withdrawn Successfully")
        else:
            print("Insufficient funds. Withdrawal failed.")

    def check_balance(self):
        print(f"Available Balance in {self.name}'s Account {self.balance}")


def main():
    accounts = {}
    num_customers = 0

    while True:
        print("=====================================")
        print("   ----Welcome to Times Bank----     ")
        print("*************************************")
        print("=<< 1. Open a New Account         >>=")
        print("=<< 2. Withdraw Money             >>=")
        print("=<< 3. Deposit Money              >>=")
        print("=<< 4. Check Customer's Balance   >>=")
        print("=<< 5. Check Number of customers  >>=")
        print("=<< 6. Exit/Quit                  >>=")
        print("*************************************")

        choice = input("Enter your choice: ")

        if choice == '1':
            account = BankAccount()
            account.open_account()
            accounts[account.name] = account
            num_customers += 1

        elif choice == '2':
            name = input("Enter customer name: ")
            if name in accounts:
                pin = input("Enter PIN number: ")
                if pin == accounts[name].pin:
                    accounts[name].withdraw()
                else:
                    print("Invalid PIN number.")
            else:
                print("Account not found.")

        elif choice == '3':
            name = input("Enter customer name: ")
            if name in accounts:
                pin = input("Enter PIN number: ")
                if pin == accounts[name].pin:
                    accounts[name].deposit()
                else:
                    print("Invalid PIN number.")
            else:
                print("Account not found.")

        elif choice == '4':
            for name, account in accounts.items():
                account.check_balance()

        elif choice == '5':
            print(f"Number of customers: {num_customers}")

        elif choice == '6':
            print("THANK YOU FOR USING OUR BANKING SYSTEM")
            print("COME AGAIN")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()