
import random

# Pick the random number:
number = random.randint(1,100)

# Set the guess to something invalid to start
guess = -1

# Set the guess count to zero
guess_number = 0

# Print a blank line, and a welcome message
print("\n")
print("Guess a number between 1 and 100!")

# Loop. As long as the guess is not equal to the number, and the guess
# count is less than 10, the user keeps guessing
while guess != number and guess_number < 10:
    if guess_number > 0:
        print("Wrong")

    # Helpful prompt to the user
    print("Guess number #" + str(guess_number) + " (Type a number and press ENTER): ")

    # Get a number from the user
    guess = int(input())

    # Increase the guess count
    guess_number = guess_number + 1

# If the loop has exited, check if it exited because the user guessed
# right, or if they ran out of guesses
if guess == number:
    print("Good job! You got it.")
else:
    print("Sorry, better luck next time.")

# Print another blank line
print("\n")

