#Bank System Simulator using OOP Python

#Features: 
#1. Sign up account, sign in, and sign out.
#2. Data insert into CSV File
#3. Deposit money
#4. Withdraw money
#5. Check balance 

class User():
    def __init__(self, name, age, gender) :
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_details(self):
        print("Personal Details: ")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)