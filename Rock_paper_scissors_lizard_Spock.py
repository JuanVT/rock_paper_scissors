# Rock-paper-scissors-lizard-Spock

import random


def name_to_number(name):

    if name == "rock":
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "This Name is not valid!"


def number_to_name(number):

    if number == 0:
        return "rock"
    elif number == 1:
        return "spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "This Number is not valid!"


def game_logic(player_choice):

    print "Player has chosen: " + player_choice

    player_number = name_to_number(player_choice)

    comp_number = random.randrange(0, 4)

    comp_choice = number_to_name(comp_number)
    print "Computer has chosen: " + comp_choice
    print

    diff = (comp_number - player_number) % 5

    if diff == 0:
        print "TIES!"
    elif diff == 3 or diff == 4:

        print "Player Wins!"

    elif diff == 1 or diff == 2:

        print "Computer Wins!"

    print

print "Select your pick:"

game_logic(raw_input())
