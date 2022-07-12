#Bank System Simulator using OOP Python

#Features: 
#1. Sign up account, sign in, and sign out.
#2. Data insert into CSV File
#3. Deposit money
#4. Withdraw money
#5. Check balance 

#Variables
accountNo = int(0)
custName = ""
bCode = ""
mobileNum = int(0)

#Functions
def createAccounts():
    accountNum = int(input("Enter your account number: "))
    custName = str(input("Name: "))
    bCode = str(input("Enter branch code: "))
    mobileNum  = int(input("Enter mobile number: "))
    global balance

    try:
        balance = float(input("Enter current balance: RM"))
    except UnboundLocalError:
        print("UnboundLocalError occured. Some variable isn't defined.")

def showAccount():
    print("Account Number: ", accountNum )
    print("Customer Name: ", custName)
    print("Branch Code: ", bCode)
    print("Mobile Number: ", mobileNum)

def deposit (amount):
    try:
        balance = balance+amount 
    except UnboundLocalError:
        print("UnboundLocalError occured. Some variable isn't defined.")
    checkBalance()

def withdraw(amount):
    try:
        balance = balance-amount 
    except UnboundLocalError:
        print("UnboundLocalError occured. Some variable isn't defined.")
    checkBalance()

def checkBalance():
    print("Current balance: RM", balance)

#Main function
userch = 'y'

while (userch == 'y'):
    print("\n----- Welcome to Bank System Simulator -----")
    print(" 1. Create account\n 2. Withdraw\n 3. Deposit\n 4. Check Balance\n 5. End Program")
    userChoice = int(input("Select any option: "))
    if (userChoice == 1):
        createAccounts()
    elif (userChoice == 2):
        userInput = float(input("Enter amount to withdraw: RM"))
        withdraw(userInput)
    elif (userChoice == 3):
        userInput = float(input("Enter amount to deposit: RM"))
        deposit(userInput)
    elif (userChoice == 4):
        checkBalance()
    elif (userChoice == 5):
        break
    else:
        print("\nPlease select any options available above.")
        print("\nDo you want to continue? \nPress y to continue \nPress n to end program")
        try: 
            userch = str(input("Enter your choice: "))
        except NameError or ValueError or TypeError:
            print("NameError/Value Error/TyperError occured. Some variable isn't defined.")
print("Ending the simulator...\nProgram end.")
