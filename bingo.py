# Import the random module to generate random numbers
import random

# Constants for the size of the bingo board and the number of rounds
BOARD_SIZE = 5
NUM_ROUNDS = 20

# Create a list of numbers to use for the bingo board
# The list should contain the numbers 1 to (BOARD_SIZE * BOARD_SIZE)
numbers = list(range(1, BOARD_SIZE * BOARD_SIZE + 1))

# Shuffle the list of numbers to create a random bingo board
random.shuffle(numbers)

# Split the list of numbers into a 2D list representing the bingo board
board = [numbers[i:i + BOARD_SIZE] for i in range(0, len(numbers), BOARD_SIZE)]

# Print the bingo board
for row in board:
    print(row)

# Create a list to store the called numbers
called_numbers = []

# Play NUM_ROUNDS rounds of bingo
for round in range(NUM_ROUNDS):
    # Generate a random number and add it to the list of called numbers
    called_number = random.choice(numbers)
    called_numbers.append(called_number)
    # Remove the called number from the list of remaining numbers
    numbers.remove(called_number)
    # Print the called number
    print("Called number:", called_number)

# Check if the player has won
# A player wins if they have a row, column, or diagonal with all numbers called
for i in range(BOARD_SIZE):
    # Check rows
    if all(number in called_numbers for number in board[i]):
        print("You won with a row!")
        break
    # Check columns
    if all(board[j][i] in called_numbers for j in range(BOARD_SIZE)):
        print("You won with a column!")
        break

# Check diagonals
if all(board[i][i] in called_numbers for i in range(BOARD_SIZE)):
    print("You won with a diagonal!")
elif all(board[i][BOARD_SIZE - i - 1] in called_numbers for i in range(BOARD_SIZE)):
    print("You won with a diagonal!")
else:
    print("Sorry, you did not win.")
