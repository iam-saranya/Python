class Bank:
    def __init__(self, name='', address='', phone=0, accno=1000, balance=0, deposit=0):
        self.name = name
        self.address = address
        self.phone = phone
        self.balance = balance
        self.deposit = deposit
        self.accno = accno
        
    def createAccount(self):
        self.name = input("Enter the name:")
        self.phone = int(input("Enter the phone no:"))
        self.address = input("Enter the address:")
        self.deposit = int(input("Enter The Initial amount (>=500 for Saving and >=1000 for current):"))
        print("\n\n\nAccount Created")
        self.accno += 1

    def showAccount(self):
        print("Account Number:", self.accno)
        print("Account Holder Name:", self.name)
        print("Account Holder Phone Number:", self.phone)
        print("Account Holder Address:", self.address)
        print("Balance:", self.balance)

    def modifyAccount(self):
        print("Account Number:", self.accno)
        self.name = input("Modify Account Holder Name:")
        self.phone = int(input("Modify Account Holder phone no:"))
        self.address = input("Modify Account Holder address:")
        self.deposit = int(input("Modify Balance:"))

    def depositAmount(self):
        amount = int(input("Enter Your Deposit Amount:"))
        self.deposit += amount
        print("The Total Balance is:", self.deposit)

    def withdrawAmount(self):
        amount = int(input("Enter Your Withdraw Amount:"))
        if amount > self.deposit:
            print("Insufficient funds!")
        else:
            self.deposit -= amount
            print("The Total Balance is:", self.deposit)

    def checkBalance(self):
        print("Balance:", self.deposit)


class Transaction(Bank):
    def loans(self):
        print("1. Educational loan")
        print("2. Agriculture loan")
        print("3. Business loan")
        choice = int(input("Enter the option:"))
        if choice == 1:
            print("1. College fees or school fees")
            print("2. Educational support")
            sub_choice = int(input("Enter your choice:"))
            self.calculate_interest(sub_choice)
        elif choice == 2:
            print("1. Crop cultivation")
            print("2. Agriculture support")
            sub_choice = int(input("Enter your choice:"))
            self.calculate_interest(sub_choice)
        elif choice == 3:
            print("1. Start-up loan")
            print("2. Personal loan")
            sub_choice = int(input("Enter your choice:"))
            self.calculate_interest(sub_choice)
        else:
            print("Enter a valid option")

    def calculate_interest(self, sub_choice):
        amount = int(input("Enter the amount:"))
        time_duration = int(input("Enter time duration:"))
        interest = (0.2 * amount * time_duration) / 100
        print("Fees amount and added interest:", interest)


class BankOperations(Transaction):
    def __init__(self):
        super().__init__()

    def run_operations(self):
        while True:
            print("\t\t\t$$$$$$$$$$$$$$$$$$$$$$$$$\n\t\t\t-------WELCOME TO YOUR BANK-------\n\t\t\t\t$$$$$$$$$$$$$$$$$$$$$$$$")
            print("\t1. NEW ACCOUNT OPEN")
            print("\t2. ALL ACCOUNT HOLDER LIST")
            print("\t3. MODIFY ACCOUNT DETAILS")
            print("\t4. CHECK BALANCE")
            print("\t5. DEPOSIT AMOUNT")
            print("\t6. WITHDRAW AMOUNT")
            print("\t7. LOAN AMOUNT")
            print("\t8. EXIT")

            choice = int(input("Select Your Option From Above Box Menu:"))

            if choice == 1:
                self.createAccount()

            elif choice == 2:
                self.showAccount()

            elif choice == 3:
                self.modifyAccount()

            elif choice == 4:
                self.checkBalance()

            elif choice == 5:
                self.depositAmount()

            elif choice == 6:
                self.withdrawAmount()

            elif choice == 7:
                self.loans()

            elif choice == 8:
                quit()

            else:
                print("Enter a valid option")


if __name__ == "__main__":
    bank_operations = BankOperations()
    bank_operations.run_operations()
