#Module:withdraw.py
def withdraw(balance):
    amt=int(input("Enter amount to withdraw (multiples of Rs.100, Rs.500):"))

    #Check if amount is valid with the amount on notes present
    if amt%100!=0:
        print("Invalid! Please enter amount in multiples of Rs.100, Rs.500")
        #Return unchanged balance
        return balance

    #Check if the amount to withdraw is more than balance in account
    if amt>balance:
        print("Insufficient balance!")
        #Returns old balance
        return balance

    else:
        #Deduct withdrawing amount from their account balance.
        balance-=amt
        print(f"Please take your cash: Rs.{amt}")
        print(f"Remaining balance: Rs.{balance}")
        #Returns new balance after reducing withdrawl amount.
        return balance