# NOTE: Code inspired and partially sourced from KiteHQ

import random

# main method
def main():
    startGame()

# introduces game and gives a selection choice
def startGame():
    print("\n*** HANGMAN SIMULATOR ***")
    print("\nWelcome to Hangman!\n")
    print("1. Easy (4-6 letter words)")
    print("2. Medium (7-9 letter words)")
    print("3. Hard (10+ letter words)")
    promptUser()

# gets the users option and calls the setHangman method
# repeats if invalid input
def promptUser():
    choice = input("\nPlease select a difficulty option: ").lower()
    if choice == 'easy' or choice == '1':
        wordType = 'easy'
    elif choice == 'medium' or choice == '2':
        wordType = 'medium'
    elif choice == 'hard' or choice == '3':
        wordType = 'hard'
    else:
        print("Cannot read input, please try again.")
        getWord()
    setHangman(wordType)

# gets the necessary random number and passes it onto the getWord and play methods
def setHangman(wordType):
    # selects a random word from the 'easy' list
    if wordType == 'easy':
        randNum = random.randrange(2, 99)
    # selects a random word from the 'medium' list
    elif wordType == 'medium':
        randNum = random.randrange(102, 199)
    # selects a random word from the 'hard' list
    elif wordType == 'hard':
        randNum = random.randrange(202, 272)
    play(getWord(randNum))

# getWord takes the random number from setHangman
# opens the library file
# reads the line, takes the random word, then assigns it to word
# @param randNum - the random number needed to take the random word
# @return word - the word that'll be guessed
def getWord(randNum):
    lib = open("wordlibrary.txt","r")
    libcontent = lib.readlines()
    word = libcontent[randNum].strip()
    return word.upper()

# takes the word and turns it into underscores
# when a letter is guessed, reveals it in the word
# when a letter is wrong, increment the attempts
# either lose after 7 attempts or win after finding the word
# @param word - the word being guessed
def play(word):
    # turn the word into underscores
    wordFin = "_" * len(word)
    guessCorrect = False
    guessLetters = ""
    attempts = 7
    # start the game
    print(display(attempts))
    print("The word is: " +wordFin+"\n")
    # stop when they run out of tries or guess correctly
    while not guessCorrect and attempts > 0:
        guess = input("Please guess a letter or word: ").upper()
        # if the guess is an alphabetical character
        if len(guess) == 1 and guess.isalpha():
            # if the guess has already been guessed, reject it
            if guess in guessLetters:
                print("You already guessed: " + guess)
            # if the guess is wrong, add it to the guess list and increment attempts
            elif guess not in word:
                print("That letter is not in the word: " + guess)
                attempts -= 1
                guessLetters = guessLetters + guess + " "
            # if the guess is right, reveal the letter and add it to the guess list
            else: 
                print("That letter IS in the word!")
                guessLetters = guessLetters + guess + " "
                wordList = list(wordFin)
                # reveals the guess
                index = [i for i, letter in enumerate(word) if letter == guess]
                for ind in index:
                    wordList[ind] = guess
                wordFin = "".join(wordList)
                # if there are no more underscores, they guessed it fully
                if "_" not in wordFin:
                    guessCorrect = True
        # if they try to guess a word, end if wrong or reveal if right
        elif len(guess) == len(word) and guess.isalpha():
            # give a warning first
            decision = input("[WARNING] Are you sure? Guessing wrong will lead to the end of the game. ").lower()
            # if they're sure, then check it
            if decision == 'yes' or decision == 'y':
                # if they're wrong, end the game and take attempts to 0
                if guess != word:
                    print("Sorry, but '" + guess + "' is not the word.")
                    attempts = 0
                # if they're right, reveal the word
                else:
                    guessCorrect = True
                    wordFin = word
        # repeat if input is invalid
        else:
            print("Not a valid input, please try again.")
        # print out the results so far
        print("Guessed letters: " + guessLetters)
        print(display(attempts))
        print("The word is: " +wordFin+"\n")
    # when the loop is done, if the guess is correct, congratulate them
    if guessCorrect:
        print("Congrats, you guessed the word: " + word)
        print("You win!")
    # if the tries are all gone, they lost
    else:
        print("Sorry, the word was: " + word + ". Best of luck next time!")
    # repeat if they want to play again
    again = input("Want to play again? ").lower()
    if again == 'y' or again == 'yes':
        main()
    else:
        print("Game ended, see you next time!")

# the visuals for the hangman board
def display(attempts):
    stages = [  # rip korean guy
                """
                   T------T
                   |      |
                   |      V
                   |      옷  
                   |   
                   |  GAME OVER.
                   |  
                --------
                """,
                # attempt 6, full body
                """
                   T------T
                   |      |
                   |      V
                   |      O
                   |     /|\   one last try...
                   |     / \\
                   |  
                --------
                """,
                # attempt 5, one limb left
                """
                   T------T
                   |      |
                   |      V
                   |      O
                   |     /|\  
                   |     /
                   |  
                --------
                """,
                # attempt 4, legs left
                """
                   T------T
                   |      |
                   |      V
                   |      O
                   |     /|\  
                   |   
                   |  
                --------
                """,
                # attempt 3, lost an arm
                """
                   T------T
                   |      |
                   |      V
                   |      O
                   |     /|
                   |   
                   |  
                --------
                """,
                # attempt 2, there goes the torso
                """
                   T------T
                   |      |
                   |      V
                   |      O
                   |      |
                   |   
                   |  
                --------
                """,
                # attempt 1, the head appears
                """
                   T------T
                   |      |
                   |      V
                   |      O 
                   |      
                   |   
                   |  
                --------
                """,
                # attempt 0: no hanging man
                """
                   T------T
                   |      |
                   |      V
                   |    
                   |      
                   |   
                   |  
                --------
                """
    ]
    return stages[attempts]

main()