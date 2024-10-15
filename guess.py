import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it!")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    # Loop until the correct number is guessed
    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!")
        except ValueError:
            print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    number_guessing_game()
