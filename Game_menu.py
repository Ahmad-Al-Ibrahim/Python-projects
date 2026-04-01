import random

# ── Magic 8-Ball ──────────────────────────────────────────────
def magic_8ball():
    answers = [
        "Yes, definitely.", "No, probably not.", "Not sure, try again.",
        "Most likely yes.", "I wouldn't count on it.", "Ask again later."
    ]
    print("\n--- Magic 8-Ball --- (type 'quit' to return to menu)\n")
    while True:
        question = input("Ask the Magic 8-Ball: ")
        if question.lower() == "quit":
            break
        if question == "":
            print("Please ask a question!")
            continue
        print("🎱", random.choice(answers), "\n")


# ── Coin Toss ─────────────────────────────────────────────────
def coin_toss():
    sides = ["Heads", "Tails"]
    print("\n--- Coin Toss --- (type 'quit' to return to menu)\n")
    while True:
        user_input = input("Press Enter to flip (or type 'quit' to exit): ").lower()
        if user_input == "quit":
            break
        print("🪙", random.choice(sides), "\n")


# ── Number Guesser ────────────────────────────────────────────
def number_guessing():
    print("\n--- Number Guesser ---\n")
    number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number from 1 to 10: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < 1 or guess > 10:
            print("Please guess a number between 1 and 10.")
        elif guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("🎉 Correct! You got it in %d attempt%s.\n" % (attempts, "s" if attempts != 1 else ""))
            break

    play_again = input("Play again? (y/n): ").lower()
    if play_again == "y":
        number_guessing()


# ── Main Menu ─────────────────────────────────────────────────
def main():
    while True:
        print("\n---- Main Menu ----")
        print("1. Magic 8-Ball")
        print("2. Coin Toss")
        print("3. Number Guesser")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            magic_8ball()
        elif choice == "2":
            coin_toss()
        elif choice == "3":
            number_guessing()
        elif choice == "4":
            print("Thanks for playing! Goodbye 👋")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


main()
