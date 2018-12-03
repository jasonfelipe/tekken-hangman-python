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
    global blanks
    global guessedLetters
    global chosenWord
    global splitWord
    global  randomNumber
    randomNumber = random.randint(0,19)
    blanks = []
    guessedLetters = []
    chosenWord = words[randomNumber]
    splitWord = list(chosenWord.lower())
    print( "-" * 50)
    print("Wins:", wins, "||","Losses:", losses)
    print("HERE'S YOUR NEXT CHALLENGER!")
    print()
    makeBlanks()
    guessCheck()

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
        global guessesLeft
        guessesLeft = 10
        gameStart()
    else: 
        print("THANKS FOR PLAYING!")
        print("-" * 50)

def win():
    global wins
    wins += 1
    print()
    print('YOU PREPARED FOR...')
    print(chosenWord)
    print("YOU BEAT", chosenWord)
    print("YOU WIN!")
    print()
    print('-' * 50)

    gameOver()

def lose():
    global losses
    losses += 1
    print()
    print('YOU HAD NO IDEA WHO YOU OPPONENT WAS...')
    print("YOUR OPPONENT WAS...")
    print(chosenWord)
    print('THEY BEAT YOU UP FOR FREE!')
    print("YOU LOSE!")
    print()
    print('-' * 50)
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
        win()
    else:
        if guessesLeft > 0:
            currentLetter = input("Please input a letter (ONE ONLY!) ")
            if currentLetter in guessedLetters:
                print('YOU ALREADY GUESSED THAT! PREDICTABLE!')
                showResults()
                print()
                guessCheck()
            else:
                if currentLetter not in alphabet:
                    print('I SAID A LETTER, AS IN SOMETHING IN THE ALPHABET!')
                    showResults()
                    print()
                    guessCheck()
                else:    
                    if len(currentLetter) > 1 and currentLetter not in alphabet:
                        print("I SAID ONE LETTER YOU FOOL!")
                        print()
                        guessCheck()
                    else:  
                        if currentLetter in splitWord:
                            rightGuess(currentLetter)
                            showResults()
                            guessCheck()

                        else:
                            wrongGuess(currentLetter)
                            showResults()
                            guessCheck()
        else:
            lose()


def rightGuess(currentLetter):
    print()
    print("YOU ARE LUCKY!")
    print()
    for index, letter in enumerate(splitWord):
        if splitWord[index] == currentLetter:
                blanks[index] = currentLetter
    guessedLetters.append(currentLetter)

def wrongGuess(currentLetter):
    print()
    print("YOU ARE WRONG YOU FOOL!")
    print()
    global guessesLeft
    guessesLeft -= 1
    guessedLetters.append(currentLetter)

def run():
    instructions()
    print()
    print("You have", guessesLeft, "guesses left...")
    gameStart()


run()