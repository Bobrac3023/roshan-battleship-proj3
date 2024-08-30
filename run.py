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
# Use for loop to fill the board with numbers from 1 to 9 in reverse order with a step of -1
for i in range(9, 0, -1):
    theBoard[i] = str(i)

""" Function to print board in a 3x3 grid"""
def print_board(theBoard):
    print(f"{theBoard[1]} | {theBoard[2]} | {theBoard[3]}")
    print("--+---+--")
    print(f"{theBoard[4]} | {theBoard[5]} | {theBoard[6]}")
    print("--+---+--")
    print(f"{theBoard[7]} | {theBoard[8]} | {theBoard[9]}")

print_board(theBoard)

