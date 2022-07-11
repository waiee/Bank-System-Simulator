#Bank System Simulator using OOP Python

#Features: 
#1. Sign up account, sign in, and sign out.
#2. Data insert into CSV File
#3. Deposit money
#4. Withdraw money
#5. Check balance 
accountNo = int(0)
custName = ""
bCode = ""
mobileNum = int(0)

def createAccounts():
    accountNum = int(input("Enter your account number: "))
    custName = str(input("Name: "))
    bCode = str(input("Enter branch code: "))
    mobileNum  = int(input("Enter mobile number: "))
    balance = float(input("Enter current balance: RM"))

def showAccount():
    print("Account Number: ", accountNum )
    print("Customer Name: ", custName)
    print("Branch Code: ", bCode)
    print("Mobile Number: ", mobileNum)

def deposit (amount):
    balance = balance+amount
    checkBalance()
    


