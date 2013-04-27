import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # convert number to a name using if/elif/else
    if number == 0:
        result = "rock"
    elif number == 1:
        result = "Spock"
    elif number == 2:
        result = "paper"
    elif number == 3:
        result = "lizard"
    elif number == 4:
        result = "scissors"
    else:
        result = "crap, you messed up bro"
    return result

    
def name_to_number(name):
    # convert name to number using if/elif/else
    if name == "rock":
        num = 0
    elif name == "Spock":
        num = 1
    elif name == "paper":
        num = 2
    elif name == "lizard":
        num = 3
    elif name == "scissors":
        num = 4
    else:
        result = 100
    return num


def rpsls(name): 
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # compute difference of player_number and comp_number modulo five
    diff = (player_number - comp_number) % 5
    print diff
    # convert comp_number to name using number_to_name
    comp_guess = number_to_name(comp_number)

    print "Player chooses " + name
    print "Computer chooses " + comp_guess

    # use if/elif/else to determine winner and print results
    if diff > 0 and diff < 3:
        print "Player wins!\n"
    elif diff > 2 and diff < 5:
        print "Computer wins!\n"
    else:
        print "Player and computer tie!\n"
    
# test the code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")