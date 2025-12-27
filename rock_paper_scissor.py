import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}
choices = tuple(emojis.keys())


def get_user_choice():
    while True:
        user_choice = input(
            "Enter your choice (r for rock, p for paper, s for scissors): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice. please try again.")


def display_choices(user_choice, computer_choice):
    print(f"You choose {emojis[user_choice]}")
    print(f"Computer chooses {emojis[computer_choice]}")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
         (user_choice == 'r' and computer_choice == 's' or
          user_choice == 'p' and computer_choice == 'r' or
          user_choice == 's' and computer_choice == 'p')):
        print("You win!")
    else:
        print("computer wins!")


def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input("Do you want to play again? (y/n): ").lower()
        if should_continue == 'n':
            print("Thanks for playing!")
            break
        elif should_continue == 'y':
            continue
        else:
            print("Invalid input, exiting the game.")
            break


play_game()
