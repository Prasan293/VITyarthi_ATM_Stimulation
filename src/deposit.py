#Module:deposit.py
def deposit(balance):
#Function to deposit money and calculating new balance.
    #Take input about amount to deposit.
    amt=int(input("Enter amount to deposit:"))
    if amt>0:
        #Adds deposit money to current balance.
        balance+=amt
        print(f"Succesfully deposited Rs.{amt}")
        print(f"New balance: Rs.{balance}")
    else:
        #Shows error for 0 or negative numbers.
        print("Invalid deposit amount")

    #Returns updated balance in main program.
    return balance