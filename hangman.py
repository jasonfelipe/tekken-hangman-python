# Hangman Psuedo Code
# Get a random word
# Fill word with blanks
# Print blank word to console.
# Give instructions
# Take a keyup or keydown event
# check if event is a letter
# if letter is correct replace the blank with the letter, print the array and guessed letters
# if letter is incorrect put the letter in the guessed array, print both guessed letters and array of blanks
# if all letters are guessed the game ends, and then it resets once the user presses a key again.
# if guesses get to 0, word is revealed, game is over, then it resets once the user presses a key again.


# TO DO: 
# FIX guessesLeft
# Show word on game over
# test if continue and next round works

import random
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 'm', 'n', 'o', "p", \
        "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
words = ["Kazuya", "Jin", "Heihachi", "Nina", "King", "Yoshimitsu", "Anna", \
        "Xiaoyu", "Kuma", "Jack", 'Lei', "Law", "Paul", "Steve", "Ogre", "Lee", "Lars", \
        "Julia", "Raven", "Miguel"]
game = False
blanks = []
guessedLetters = []
randomNumber = random.randint(0,19)
chosenWord = words[randomNumber]
splitWord = list(chosenWord.lower())
guessesLeft = 10
wins = 0
losses = 0


def instructions():
    print( "-" * 50)
    print('___________     __    __')                  
    print('\__    ___/___ |  | _|  | __ ____   ____')  
    print('  |    |_/ __ \|  |/ /  |/ // __ \ /    \\') 
    print('  |    |\  ___/|    <|    <\  ___/|   |  \\')
    print('  |____| \___  >__|_ \__|_ \\\___  >___|  /')
    print('             \/     \/    \/    \/     \/ ')
    print()    
    print("Welcome to the King of Iron Fist Tournament!")
    print("Can you figure out who your opponent is?")
    print("Input a letter and fill in the blanks!")
    print("If you lose, I'll throw you into a volcano...!")
    # print( "-" * 50)

def gameStart():
    game = True
    blanks = []
    guessedLetters = []
    chosenWord = words[randomNumber]
    splitWord = list(chosenWord.lower())
    print( "-" * 50)
    print("HERE'S YOUR NEXT CHALLENGER!")
    print()
    makeBlanks()
    guessCheck()

def gameEnd():
    game = False

def makeBlanks(): 
    # For loop to get index and each item
    for index, letter in enumerate(chosenWord):
        # print(letter)
        # print(index)
        blanks.append("_")
    print(blanks)


def gameOver():
    userContinue = input("Would you like to continue? Y/n ")    
    if userContinue.upper() == "Y": 
        guessesLeft = 10
        gameStart()
    else: 
        print("THANKS FOR PLAYING!")
        print("-" * 50)

def win(wins):
    wins += 1
    print("YOU WIN!")
    gameOver()

def lose(losses):
    losses += 1
    print("YOU LOSE!")
    gameOver()

def showResults():
    print('-' * 50)
    print("Wins:", wins, "||","Losses:", losses)
    print("HERE'S YOUR CURRENT CHALLENGER!")
    print(blanks)
    print()
    print("Guesses Left:", guessesLeft)
    print("Guessed Letters:", guessedLetters)
    print()


def guessCheck():
    if "_" not in blanks:
        win(wins)
    else:
        if guessesLeft > 0:
            currentLetter = input("Please input a letter (ONE ONLY!) ")
            if len(currentLetter) > 1:
                print("I SAID ONE LETTER YOU FOOL!")
                guessCheck()
            else:  
                if currentLetter in splitWord:
                    rightGuess(guessesLeft, currentLetter)
                    showResults()
                    guessCheck()

                else:
                    wrongGuess(guessesLeft, currentLetter)
                    showResults()
                    guessCheck()
        else:
            gameEnd()
            gameOver()


def rightGuess(guessesLeft, currentLetter):
    print()
    print("YOU ARE LUCKY!")
    print()
    guessesLeft -= 1
    for index, letter in enumerate(splitWord):
        if splitWord[index] == currentLetter:
                blanks[index] = currentLetter
    guessedLetters.append(currentLetter)
    return guessesLeft

def wrongGuess(guessesLeft, currentLetter):
    print()
    print("YOU ARE WRONG YOU FOOL!")
    print()
    guessesLeft -= 1
    guessedLetters.append(currentLetter)
    return guessesLeft

def run():
    instructions()
    print()
    print("You have", guessesLeft, "guesses left...")
    gameStart()


run()