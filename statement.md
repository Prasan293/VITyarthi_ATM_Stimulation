# Official Project Statement

Student Name: Prasan Prabhakar Rai

Project Name: ATM Simulation App

### Problem Description

The common industry practice while writing basic console applications in classes is to keep all code under one single python file. While acceptable for smaller projects, such approach may lead to readability issues for bigger programs. This project aims to address this exact problem. Under this project, the code is split into 5 different files with each file's code being dedicated to a specific part of the application. This improves maintainability as a bug in the withdrawal function now only requires checking of the withdraw.py file.

Another industry-level problem that this project touches on is the robustness of the code. When writing applications that take input from users, there is a possibility of receiving invalid input data. Failure to implement proper exception handling mechanisms will result in the program crashing with an unhandled exception error. This project will focus on the implementation of protective measures in order to prevent such crashes.

### Scope

The scope of this project is to develop a proof-of-concept prototype of a bank ATM system. The application will be designed to handle regular teller operations:

• The program will force the user to enter a valid PIN before displaying any account information

• The program will prevent outsiders from guessing the PIN

• The program will be able to share variable values between scripts (i.e. update the account balance across different files)

• The program will prevent outsiders from withdrawing large sums of cash

• The program will perform denomination arithmetic checks

### Limitations

Due to the nature of this project being a school assignment, it does not cover everything that a working example would require:

• The project does not use database software to record entries. All data is lost upon termination of the main script

• Upon closing the terminal window, the account balance reverts to Rs. 50000. This happens because no cloud storage solutions are used to save the data

• The application uses no graphic interfaces and is strictly text-based. All visual elements are placed in a black terminal window

### Intended Audience

This project is developed with the intended audience of my lab instructors and examiners. This application serves to demonstrate my understanding of fundamental concepts of programming. During this assignment, I learned how to share variables between python files without creating global variables. Additionally, the project demonstrates my understanding of loops and mathematical functions. The application may also be useful to other students who are interested in seeing practical examples of said concepts.