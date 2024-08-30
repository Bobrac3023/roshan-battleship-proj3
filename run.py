# import datetime module from python
import datetime
x = datetime.datetime.now()
# display current year,month andday.hour,minute,second,and microsecond in UTC
print(x)

# import random module from python
import random
print ( " !!!! Welcome to the Battleship game !!!!")

# Create  list with 10 spaces (index 0 to 9). Index 0 is unused and assign to variable theBoard
theBoard = [" "] * 10
# Use "for loop" to fill the board with numbers from 1 to 9 in reverse order with a step of -1
for i in range(9, 0, -1):
    theBoard[i] = str(i)

""" Function to print 3x3 grid"""
def print_grid(theBoard):
    print(f"{theBoard[1]} | {theBoard[2]} | {theBoard[3]}")
    print("--+---+--")
    print(f"{theBoard[4]} | {theBoard[5]} | {theBoard[6]}")
    print("--+---+--")
    print(f"{theBoard[7]} | {theBoard[8]} | {theBoard[9]}")

""" Check if user_input matches random_generator number"""
def match(random_generator, user_input):
 return random_generator == user_input

""" Main function to run the game """
def main():
    # generate random integer values between 1-9
    value = random.randint(1, 9)  
    print("Computer Says - Ship is hidden at position between 1 to 9:")  
    
    while True:
        # try and except method for input type validation 
        try:
            codegenerator = int(input("Dear Player: Please enter a number between 1 to 9 to guess the ship position : "))
        except ValueError:
            print("The number must be a numeric value between 1 to 9")
            continue  
        if codegenerator < 1 or codegenerator > 9:
            print("The number must be between 1 and 9.")
            continue
        # Compare result , mark "H" for hit or "X" for miss and "L" for ship location ( in case of a miss) 
        if match(value, codegenerator):
            print("You have hit the jackpot! Well done !!!")
            theBoard[codegenerator] = "H"  # Mark a hit on the board
        else:
            print("OOPS you missed !!!. The ship's location is at L")
            theBoard[codegenerator] = "X"  # Mark X for a miss on the board
            theBoard[value]="L" # Mark "L" for the correct position
        # Print the updated grid
        print_grid(theBoard)
           # Seek user input to  continue or exit the game
        while True:
            user_input = input('Do you wish to continue? yes/no: ').strip().lower()
            if user_input == 'yes':
                print('You chose to continue.')
                 # generate random integer values between 1-9
                value = random.randint(1, 9)
                break
            elif user_input == 'no':
                print('Sorry to see you stop. Goodbye!')
                return  # Exit the function and end the game
            else:
                print('Please type "yes" or "no".')

""" Main function to start the game"""
main()

