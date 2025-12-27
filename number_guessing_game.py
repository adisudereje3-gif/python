import random
guess_number = random.randint(1, 100)
while True:
    try:
        guess = int(input("please enter your guess number between 1 to 100: "))
        if guess < guess_number:
            print("Too low! try again.")
        elif guess > guess_number:
            print("Too high! try again.")
        else:
            print("Congratulations! you guessed the correct number.")
            break
    except ValueError:
        print("Invalid input. please enter a valid integer.")
