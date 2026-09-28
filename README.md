# ATM Simulation Project

This is my project for the portal upload. It is an ATM machine that works inside your terminal window. I used Python to make it. I did not put everything in one long file. That would be very messy. Instead, I made a folder called src. I put separate small files inside it. One file does the PIN checking. Another file checks your balance. Then there is one for putting money in, and another for taking money out. 

The main script is called main.py and it sits outside the folder. It controls the whole flow. It imports everything from the other files. It keeps running in a loop until you type option 4 to exit.

## Things This Code Can Do

I wrote a lot of logic rules to make it act like a real bank machine. 

First, it asks for your secret PIN. The PIN is hardcoded to 1234 right now. If you type the wrong numbers, it tells you that you are wrong. It tracks your attempts. It starts at 3 attempts. Every time you guess wrong, it subtracts 1 from your total attempts. If you fail 3 times, it blocks you out. It prints a big blocked message. Then the whole script just stops running. You cannot try again unless you restart the program.

If you type the right PIN, it lets you see the menu screen. The menu has options. You can check your account balance. The starting balance is Rs. 50000. It is a big number so you can test withdrawals easily.

When you deposit money, it asks how much. You must type a positive number. If you try to type a negative number or zero, it says it is an invalid amount. It does not crash. It just sends you back to the main menu. If it is a good number, it adds it to your balance. Then it prints out your new balance.

When you want to take cash out, it checks two things. It checks if you have enough money. If you try to take Rs. 60000 when you only have Rs. 50000, it prints a message saying you have insufficient balance. It also checks the cash notes. A real ATM only has certain bills. So my code uses a modulo math check. It makes sure your amount can be divided by 100 evenly. If you type 350, it tells you that it is invalid. You can only ask for things like 100, 200, 500, or 1000.

##Technologies Used

Python 3
Command-Line Interface (CLI)
Git
GitHub

## How to Run It

It is very easy to start this application on your computer.

1. First you need to download Python. Make sure it is Python 3.
2. Put all these files together in one folder on your computer desktop.
3. Open your command prompt or terminal application.
4. Use the cd command to navigate inside that project folder.
5. Type this command and hit enter:
   python main.py

Sometimes if your terminal has a weird path error you might need to type python3 main.py instead. It depends on how you installed it.

## Testing Steps

You can test it yourself to see if my validation works.

First test: Type 1111 when it asks for the PIN. It should say you have 2 attempts left. Type 2222 next. It should say 1 attempt left. Type 3333 on the last turn. The program will print BLOCKED and exit completely.

Second test: Start the program again. Type the correct PIN which is 3546. Press 3 to choose withdrawal. Type 450. The terminal will tell you it is an invalid amount because it needs to be a multiple of 100 or 500.

Third test: Try to withdraw Rs. 90000. It will say insufficient balance because you only start with 50000.
