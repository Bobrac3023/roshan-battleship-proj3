import random

import datetime

from pytz import timezone

# display current date and time
x = datetime.datetime.now()
format = "%m-%d-%Y %A %H:%M %p %z"

# Convert to Asia/Dubai time zone
native = x.astimezone(timezone('Asia/Dubai'))
print(native.strftime(format))


print( " !!!! Welcome to the Battleship game !!!!")

# Create list with 10 spaces(index 0 to 9),assign to variable the_board
the_board = [" "] * 10

# fill board with nos from 1 to 9 in reverse order,step of -1
for i in range(9, 0, -1):
    the_board[i] = str(i)


def print_grid(the_board):
    """ Function to print 3x3 grid"""
    print(f"{the_board[1]} | {the_board[2]} | {the_board[3]}")
    print("--+---+--")
    print(f"{the_board[4]} | {the_board[5]} | {the_board[6]}")
    print("--+---+--")
    print(f"{the_board[7]} | {the_board[8]} | {the_board[9]}")


def match(random_generator, user_input): 
    """ Check if user_input matches random_generator number"""
    return random_generator == user_input


def main():
    """ Main function to run the game """
    # generate random integer values between 1-9
    value = random.randint(1, 9)  
    print("Computer Says - Ship is hidden at position between 1 to 9:")  
    
    while True:
        # try except method for input validation 
        try:
            # add new line character inside text for odd quirk issue
            code_generator = int(input("Enter number to guess ships position(1-9) :\n "))
        except ValueError:
            print("The number must be numeric value between 1 to 9")
            continue
 
        if code_generator < 1 or code_generator > 9:
            print("The number must be between 1 and 9.")
            continue

        # Compare result , mark "H" or "X" and "L"
        if match(value, code_generator):
            print("You have hit the jackpot! Well done !!!")
            the_board[code_generator] = "H"  # Mark a hit on the board
        else:
            print("OOPS you missed !!!. The ship's location is at L")
            the_board[code_generator] = "X"  # Mark X for a miss on the board
            the_board[value]="L" # Mark "L" for the correct position

        # Print updated grid
        print_grid(the_board)

        # Seek user input to  continue or exit the game
        while True:
            # add new line character inside text for odd quirk issue
            user_input = input('Do you wish to continue? yes/no:\n ').strip().lower()
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
if __name__ == "__main__":
    main()

