#  File: GuessingGame.py

#  Description: Program guesses the number the user is thinking of as long as its between 1 and 100 in 7 tries or under.

#  Student Name: Matthew Yap

#  Student UT EID: my5476

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 4/12/2016

#  Date Last Modified: 4/13/2016

def main():
    
    #   define variables and counter
    low = 1
    high = 100
    middle = (high + low)//2
    counter = 1
    
    #   prompt the user
    print("Guessing Game")
    print()
    print("Think of a number between 1 and 100 inclusive.")
    print("And I will guess what it is in 7 tries or less.")
    print()
    opening = (input("Are you ready? (y/n): "))
    
    #   while statement to make sure the user's input is one of the two choices
    while opening != "y" and opening != "n":
        opening = (input("Are you ready? (y/n): "))
        
    #   while statement to exit the program if the user doesn't want to play
    if opening is "n":
        print("Bye")
        return
    
    #   while statement to start the game if the user chooses to
    if opening is "y":
        print("Guess", str(counter) + ": The number you thought was", middle)
        adjust = (input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))
        print()

        #   while statement to make sure that the program has 7 triess
        while counter < 7:

            #   while statement to make sure the user's input is one of the 3 choices
            while adjust != "1" and adjust != "0" and adjust != "-1":
                print("Guess", str(counter) + ": The number you thought was", middle)
                adjust = (input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))
                print()

            #   Ends the program when the user inputs 0
            if adjust == "0":
                print("Thank you for playing the Guessing Game.")
                quit()

            #   adjusts the program's guess when it's too high
            elif adjust == "1":
                high = middle
                middle = (low + high)//2
                counter = counter + 1
                print("Guess", str(counter) + ": The number you though was", middle)
                adjust = (input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))
                print()

            #   adjusts the program's guess when it's too low
            elif adjust == "-1":
                low = middle
                middle = (low + high)//2
                counter = counter + 1
                print("Guess", str(counter) + ": The nubmer you though was", middle)
                adjust = (input("enter 1 if my guess was high, -1 if low, and 0 if correct: "))
                print()

    #   If the program doesn't guess correctly in 7 turns it prints this message
    print("Either you guessed a number out of range or you had an incorrect entry.")

main()
               
