#Importing all function from src folder for use
from src.check_balance import check_balance
from src.deposit import deposit
from src.valid_pin import valid_pin
from src.withdraw import withdraw

#To run ATM stimulator
def main():
    #Welcome Message
    print("\t====Welcome to the ATM====")

    #Checking PIN before starting ATM Stimulator
    if not valid_pin():
        return

    #Setting up starting balance from before to make it easier
    acc_balance=50000

    #If PIN is correct, this infinite loop runs to keep showing the menu screen
    while True:
        #Main menu
        print("\t----ATM Main Menu----")
        print("1. Check balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. EXIT")

        #Taking choice from the user
        choice=input("Select option(1-4):")

        #Running the functions from modules according to the user's choice
        if choice=="1":
            print(f"Your current balance is Rs.{acc_balance}")

        elif choice=="2":
            acc_balance=deposit(acc_balance)

        elif choice=="3":
            acc_balance=withdraw(acc_balance)

        elif choice=="4":
            print("Thank YOU, Goodbye")
            break

        else:
            print("Invalid selection. Please choose from 1-4")

#Standard python program,to run main() function automatically.
if __name__=="__main__":
    main()

        
        