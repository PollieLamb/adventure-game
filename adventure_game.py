from socket import if_nameindex
from tabnanny import check
import time
import random

# answer = ["yes", "Y", "yes", "y"]
# answer = ["no", "N", "no", "n"] these aren't needed, but were a good place to start

#This function is needed to print messages
def print_pause(message, pause=2):
    print(message)
    time.sleep(pause)

#This is a single function to handle all the user input
#the options parameter handles the choices that the user can respond with
#that are accepted as valid choices
def valid_input(message, options):
    while True:
        answer = input(message)
        if answer in options:
            return answer
        else:
            print_pause("\nYou typed the wrong input. try again!\n")


def intro():
    print("""
    WELCOME! LET'S START THE ADVENTURE

    You are standing outside in the middle of nowhere in an eerie dark damp
    forest.
    The woman was mystified and could not figure out where to find shelter
    and hide from her kidnappers
    """)

#moves along the game based on the player's answer
def play():
    answer = valid_input("Will you provide shelter to her? (yes / no)\n", ["yes", "no"])
    if answer == "yes":
        shelter()
    elif answer == "no":
        kidnap()


def shelter():
    print_pause("""\nAfter 2 minutes, the kidnappers come
    to the door asking if
    he could come in?""")
    answer = valid_input("Will you say (yes / no)\n", ["yes", "no"])
    if answer == "yes":
        print_pause("""\nYou  were afraid for your own
        life and did not know the
                situation.. The  kidnapper was let in &
                You won the Game""")
        play_again()
#the win/lose text options should be changed, as they seem reversed
    elif answer == "no":
        print_pause("""\nYou helped the kidnapper.
        Now the woman is being kidnapped
        in front of your eyes. GAME OVER""")
        coins = random.randint(0, 5) #one fun way to use a random element
        print_pause(f"The kidnapper pays you {coins} for helping him out.")
        play_again()


def kidnap():
    print("\nNow, he is trying to kidnap you too.")
    answer = valid_input("Will you fight the attacker = ? (yes / no)\n", ["yes", "no"])
    if answer == "yes":
        print("""\nYippers! You fight back and was trying to save the
        woman's life. You win!""")
        play_again()
    elif answer == "no":
        print("""\nSorry! You got kidnapped and resisted being
        kidnapped..
        GAME OVER""")
        play_again()
        #calls the play again function after you lose
    # else:
    #     print("\nYou typed the wrong input. try again!")
    #this isn't needed due to the valid_input function



# print_message("you entered an invalid entry,good bye!")
# def adventure_game():
#     user_input= input("Answer yes or no to the kidnapper\n").lower()
#     if "yes" in user_input:
#         print_message("You won the game!")
#     elif "no" in user_input:
#         print_message("So you helped the kidnapper, you lost, Game Over!")
#         random.randint(0,5)
#         end_of_game()
#     else:
#         print_message("That is not a valid entry, good bye!")
#         adventure_game()
# adventure_game()



#this function is for handling game over, and restarting the game
def play_again():
    answer = valid_input("Would you like to play again? yes or no\n", ["yes", "no"])
    if "yes" == answer:
        print_pause("Yay, continue to game")
        play_game()
    elif "no" == answer:
        print_pause("Cool beans, good bye!")
        exit(0)

def play_game():
    intro()
    play()
    play_again()


if __name__ == "__main__":
    play_game()