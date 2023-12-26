import random

def generate_random_number():
    return random.randint(10000, 99999)

def evaluate_guess(random_number, user_guess):
    result = ''
    for i in range(5):
        if user_guess[i] == random_number[i]:
            result += 'C'
        elif user_guess[i] in random_number:
            result += 'B'
        else:
            result += 'A'
    return result

def main():
    random_number = str(generate_random_number())
    max_attempts = 5
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("Try to guess the 5-digit number.")

    while attempts < max_attempts:
        user_guess = input("Enter your guess: ")

        if len(user_guess) != 5 or not user_guess.isdigit():
            print("Please enter a valid 5-digit number.")
            continue

        attempts += 1
        feedback = evaluate_guess(random_number, user_guess)

        print(f"Attempt {attempts}: {feedback}")

        if feedback == 'CCCCC':
            print(f"Congratulations! You guessed the number {random_number} correctly!")
            break

    if attempts == max_attempts:
        print(f"Sorry, you've reached the maximum number of attempts. The correct number was {random_number}.")

if __name__ == "__main__":
    main()
