import random

print("🎲 Welcome to the Number Guessing Game! 🎲")
print("I'm thinking of a number between 1 and 10...")

while True:
    secret_no = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess > secret_no:
                print("Too high! Try again.")
            elif guess < secret_no:
                print("Too low! Try again.")
            else:
                print(f"🎉 Just right! The number was {secret_no}.")
                print(f"You guessed it in {attempts} tries!")
                break
        except ValueError:
            print("Oops! Please enter a valid number.")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 👋 See you next time.")
        break
