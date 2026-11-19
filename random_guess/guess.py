import random

def get_guess():
    while True:
        try:
            guess = int(input("Guess a number from 1 to 100: "))
            if 1 <= guess <= 100:
                return guess
            print("Please enter a number from 1 to 100.")
        except ValueError:
            print("Please enter a whole number.")

def play_game():
    answer = random.randint(1, 100)
    attempts = 0
    while True:
        guess = get_guess()
        attempts += 1
        if guess < answer:
            print("Too low.")
        elif guess > answer:
            print("Too high.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

def main():
    play_game()

if __name__ == "__main__":
    main()