#   A program to help you solve your Wordle Puzzle!
#	Caleb Gibson
#	2/24/2022
#	5:07 am

#SETUP -----------------------------

#Imports
import random

#Import the Dictionary file by reading in a file 
f=open("dictionary.txt", "r")
Lines = [line.rstrip() for line in f]


#Create a list of possible passwords
possibleWords = []
wordsToRemove = []

#read in all entries from the reader object to the array
for x in Lines:
	if(len(x) != 5):
		wordsToRemove.append(x)

for word in wordsToRemove:
	Lines.remove(word)

#FUNCTIONS -------------------------

#Function to narrow down
def HelloNarrow():
	#Explain to the user
	print("\nIn order to narrow down our choices, go ahead and guess")
	print("a valid 5-letter word in the Wordle app/website.\n")
	print("Do you need an example of a valid 5-letter word? (y/n)")

	#take in the users choice
	choiceValidFiveLetterWord = input()
	if(choiceValidFiveLetterWord == 'y'):
		#grab a random 5 letter word from the dictionary
		print()
		print(random.choice(Lines) + "\n")

	while (choiceValidFiveLetterWord != 'y' and choiceValidFiveLetterWord != 'n'):
		print("Please only enter the letter \'y\' or \'n\'. ")
		choiceValidFiveLetterWord = input()

	print("We will need to use any possible grey, yellow, or green colors")
	print("to be able to reduce the possible word choices.\n")
	Guess()

#Function to play the game for you
def HelloPlay():
	#Explain to the user
	print("\nI will go ahead and play the game for you, but need some help.")
	print("After every guess I make, I will need you to enter the word into the Wordle game/site.")
	print("I will need you to give me the grey letters, the yellow letters, and the green letters")

	choice = input("Please enter \'y\' to continue: ")
	print(choice)
	if(choice == 'y'):
		initialGuess()
	#The way to actually make the computer reduce possible letters
	autoRun = True
	for alpha in range(6):	
		Guess(autoRun)
		AutoGuess()


#Function for the first Computer guess
def initialGuess():
	print("I am going to guess a random word for you to try: " + random.choice(Lines))

def AutoGuess():
	print("My next guess: " + random.choice(Lines))

#Function for reducing array by eliminating greys
#Overloaded function to reduce Greys
def reduceGreys(greyLetter, yellowLetter = None):
	#edge case if there are multiple of a letter (ee) and one is grey while the other is yellow
	#Check to make sure the grey is not also a yellow
	for y in Lines:
		if greyLetter in y:
			if yellowLetter is None:
				wordsToRemove.append(y)
			else:
				if greyLetter != yellowLetter:
					wordsToRemove.append(y)

#Function for reducing array based on greens
def reduceGreens(greenLetter, index):
	#remove entries where green is not in the correct spot
	for y in Lines:
		if not (y[index] == greenLetter):
			wordsToRemove.append(y)

#Function for reducing array based on yellows
def reduceYellows(yellowLetter, index):
	#remove entries from array that contain the grey letter
	for y in Lines:
		if not (yellowLetter in y):
			wordsToRemove.append(y)
		if (y[index] == yellowLetter):
			wordsToRemove.append(y)
			
def removeWords():
	for words in wordsToRemove:
		if(words in Lines):
			Lines.remove(words)

#Function to run through a guess
def Guess(autoRun = None):
	print("Please enter the amount of yellow letters in that guess.")
	numYellow = int(input(">: "))

	#make the yellow entry null to begin
	yellowLetter = None

	for x in range(numYellow):
		yellowLetter = input("Please enter a yellow letter: ")
		index = int(input("Please enter the index of the yellow letter: "))
		reduceYellows(yellowLetter, index)

	print("Please enter the amount of grey letters in that guess.")
	numGrey = int(input(">: "))
	for x in range(numGrey):
		greyLetter = input("Please enter a grey letter: ")
		print(greyLetter)
		reduceGreys(greyLetter, yellowLetter)

	print("Please enter the amount of green letters in that guess.")
	numGreen = int(input(">: "))
	for x in range(numGreen):
		greenLetter = input("Please enter a green letter: ")
		index = int(input("Please enter the index of the green letter: "))
		reduceGreens(greenLetter, index)

	#Remove words from array
	removeWords()

	#Ask if the user would like to see the current list of usable words
	print()
	chooseList = input("Would you like to see a list of valid words? (y\\n)")
	while not(chooseList == 'y' or chooseList == 'n'):
		chooseList = input("Choose \'y\' or \'n\'")
	if(chooseList == 'y'):
		print()
		print("-------------------")
		for words in Lines:
			print (words)
		print("-------------------")

	#Ask the user if they would like to guess again
	goAgain = input("Would you like to guess another word (y/n) ?")
	while (goAgain != 'y' and goAgain != 'n'):
		goAgain = input("Enter \'y\' or \'n\' : ")
	#If yes, run the guess function
	if goAgain == 'y':
		if(autoRun is None):
			Guess()

#Welcome the player to the game
print("\n\nWelcome to the Wordle Helper Program!\n\n")
print("Would you like me to help narrow down the posible words you should try?\n")
print("Or would you like me to try and play for you?\n")
print("Type \'n\' for narrowing down or \'s\' for me to solve the puzzle!\n")
choice = input(">: ")
print (choice)
if(choice == 's'):
	#run the function for solving
	HelloPlay()

if(choice == 'n'):
	#run the function for narrowing down
	HelloNarrow()