# Rock-paper-scissors-lizard-Spock

import random

game_elements = ['rock', 'paper', 'scissors', 'lizard', 'spock']


def game_logic():
    print "Select your pick:"
    player_choice = raw_input()

    if player_choice not in game_elements:
        print "That choice is not available, zoquete! Try again..."
        return game_logic()

    print "Player has chosen: " + player_choice

    player_number = game_elements.index(player_choice)

    comp_number = random.randrange(0, 4)

    comp_choice = game_elements[comp_number]

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

game_logic()
