#Module:valid_pin.py
def valid_pin():
    #Assigning correct pin to check.
    correct_pin=1234
    #Total attempts given to user to enter pin that matches with correct_pin.
    attempt=3

    #Let's user enter PIN as many times as the number of attempts left.
    while attempt>0:
        #Takes PIN from user to match with correct_pin
        enter_pin=int(input("Enter 4-digit pin:"))
        #If PIN matches, let's the user use stimulator
        if enter_pin==correct_pin:
            print("\tPin Accepted!")
            return True
        else:
            #When wrong,attempts decrease by 1.
            attempt-=1
            print(f"Wrong PIN. You have {attempt} attempts left")

    #If they run out of all attempts,they are blocked and program stops.        
    print("Too many incorrect attempts. \n\t======BLOCKED!======")
    return False    