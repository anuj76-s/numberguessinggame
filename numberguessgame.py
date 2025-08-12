import random

def describe_game():
    print("🎮 Welcome to the number guessing game.")
    print("Let's see if you can guess it right.")

def choose_level():
    while True:
        level = input("choose your level(E/M/H): ").strip().lower()
        if level == 'e':
           return 0, 50, 10
        elif level == 'm':
           return 0, 100,5
        elif level == 'h':
           return 0, 1000, 3
        else:
           print("Invalid choice.Enter (E/M/H))")

def get_user_guess(lower,upper,attempts_num,max_attempts):
    while True:
        try:
            guess = int(input(f"attempts {attempts_num}/{max_attempts}:guess a number between {lower} and {upper}: "))
            if lower <= guess <= upper:
                return guess
            else:
                print(f"enter number between {lower} and {upper}.")
        except ValueError:
            print("Input invalid.Enter a valid number.")

def play_game():
    describe_game()
    lower, upper, max_attempts = choose_level()
    answer = random.randint(lower,upper)
    attempts = 0

    while attempts < max_attempts:
        guess = get_user_guess(lower,upper,attempts + 1,max_attempts)
        attempts += 1

        if guess < answer:
            print("Too low!Try again.")
        elif guess > answer:
            print("Too high!Try again.")
        else:
            print("🎇 you won!")
            return

    if attempts == max_attempts and guess != answer:
        print(f"Sorry😔 you have used all {max_attempts} attempts.The correct answer is {answer}.")

def ask_replay():
    while True:
        replay = input("do you want to play again? (Y/N): ").strip().lower()
        if replay == 'y':
            return True
        elif replay == 'n':
            return False
        else:
            print("please type y or n.")

def main_game():
    while True:
        play_game()
        if not ask_replay():
            print("Thank you for playing!👋")
            break

main_game()
print("come soon")
