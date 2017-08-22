import random

picks = ["rock", "paper", "scissors"]


player_pick = raw_input("Pick your selection: ")


computer_pick = random.choice(picks)
print "Computer has chosen:",computer_pick

#ignore (still working in that function)
# def rock_paper_scissors():

#     if player_pick == picks:
#         return player_pick
#     else:
#         print "You can't pick that."
#
#     if (player_pick == "scissors") and (computer_pick == "rock"):
#
#         print "Computer Wins!"
#
#     elif (player_pick == "scissors") and (computer_pick == "paper"):
#
#         print "Player Wins!"
#
#     elif (player_pick == "rock") and (computer_pick == "paper"):
#         print "Computer Wins!"
#
#     elif (player_pick == "rock") and (computer_pick == "scissors"):
#         print "Player Wins!"
#
#     elif (player_pick == "paper") and (computer_pick == "rock"):
#         print "Player Wins!"
#
#     elif (player_pick == "paper") and (computer_pick == "scissors"):
#         print "Computer Wins!"
#
# # Computer Possibilities:
#
#     elif (computer_pick == "scissors") and (player_pick == "rock"):
#         print "Player Wins!"
#
#     elif (computer_pick == "scissors") and (player_pick == "paper"):
#         print "Computer Wins!"
#
#     elif (computer_pick == "paper") and (player_pick == "rock"):
#         print "Computer Wins!"
#
#     elif (computer_pick == "paper") and (player_pick == "scissors"):
#         print "Player Wins!"
#
#     elif (computer_pick == "rock") and (player_pick == "paper"):
#         print "Player Wins!"
#
#     elif (computer_pick == "rock") and (player_pick == "scissors"):
#         print "Player Wins!"
#
#     else:
#         print "No Way"

# rock_paper_scissors()