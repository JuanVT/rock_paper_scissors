
# name= PLAYER
# name1 = COMPUTER


name = "scissors"
name1 = "rock"


def pick_jugador(name):

    if (name == "rock") or (name == 'paper') or (name == "scissors"):

        print "Player has choosen " + str(name) + "!"

    else:

        print "This Name is not valid!"

def pick_maquina(name1):


    if (name1 == "rock") or (name1 == 'paper') or (name1 == "scissors"):

        print 'Computer has choosen ' + str(name1) + "!"

    else:
        print "This Name is not valid!"



# All the Possibilities

def psr():

    if (name == name1):
        print "Ties!"

    elif (name == "scissors") and (name1 == "rock"):

        print "Computer Wins!"

    elif (name == "scissors") and (name1 == "paper"):

        print "Player Wins!"

    elif (name == "rock") and (name1 == "paper"):
        print "Computer Wins!"

    elif (name == "rock") and (name1 == "scissors"):
        print "Player Wins!"

    elif (name == "scissors") and (name1 == "rock"):
        print "Computer Wins!"

    elif (name == "scissors") and (name1 == "paper"):
        print "Player Wins!"
    else:
        print "No Way"

print
pick_jugador(name)
pick_maquina(name1)
print
psr()