#  This is a bot to play rock paper scissor using CLI
import random


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def game():

    rock = '''
        ________
    ---'   ____ )
        (_____)
        (_____)
        (____)
    ---(___)
    '''

    paper = '''
        _______
    ---'   ____)__
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)___
            _______)
        ____________)
        (____)
    ---.__(___)
    '''
    game_images = [rock, paper, scissors]

    user_choice = int(
        input("0 : Rock | 1 : Paper | 2 : scissors \nYour choice  : "))
    print(colored(200, 200, 50, game_images[user_choice]))

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(colored(255, 20, 250, game_images[computer_choice]))

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")


def choice():
    choice = input("TRY AGAIN (Y/N) : ").lower()
    return choice


game()
ask = choice()

while ask == 'y':
    game()
    ask = choice()
