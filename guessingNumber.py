# Basic guessing game

import simplegui
import random
import math

# initialize global variables
availGuesses = 0
rand_number = 0

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
	global availGuesses
	availGuesses = 7
	global rand_number
	rand_number = random.randrange(0, 100)
	print "New Game. Range is from 0 to 100"
	print "Number of remaining guesses is " + str(availGuesses) + "\n"

def range1000():
    # button that changes range to range [0,1000) and restarts
	global availGuesses
	availGuesses = 10
	global rand_number
	rand_number = random.randrange(0, 1000)
	print "New Game. Range is from 0 to 1000"
	print "Number of remaining guesses is " + str(availGuesses) + "\n"
    
def get_input(guess):
    # main game logic goes here
    guess = int(guess)
    print "Guess was " + str(guess)
    if guess == rand_number:
    	print "Correct!"
    	return

    global availGuesses
    availGuesses = availGuesses - 1

    print "Number of remaining guesses is " + str(availGuesses)
    if availGuesses == 0:
    	print "You ran out of guesses. The number was " + str(rand_number)
    elif guess > rand_number:
    	print "Lower!\n"
    elif guess < rand_number:
    	print "Higher!\n"
    else:
    	print "WTF\n"

    
# create frame
frame = simplegui.create_frame("Guess the number!", 200, 200)

# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", get_input, 200)

frame.start()
