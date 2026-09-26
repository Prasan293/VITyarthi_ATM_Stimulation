#Import test modules
import src.deposit as deposit_module
import src.withdraw as withdraw_module

#Fake input to test
fake=[]

def ever(p=""):
    return fake.pop(0)

#Putting function into modules
deposit_module.input=ever
withdraw_module.input=ever

print("\t----Starting Test----")

#Testing deposit function
fake=["5000"]
if deposit_module.deposit(10000)==15000:
    print("Deposit Test: PASSED")
else:
    print("Deposit Test: FAILED")

#Testing withdraw function
fake=["3000"]
if withdraw_module.withdraw(10000)==7000:
    print("Withdraw Test: PASSED")
else:
    print("Withdraw Test: FAILED")