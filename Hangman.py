import random

secret_words='ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split(" ")

hangman_fig=['''-----
                    |
                    |
                    |
                    |''',
          '''-----
               o |
                 |
                 |
                 |''',
        ''' -----
              o |
              | |
              | |
              | |''',
        ''' -----
              o |
             /| |
              | |
              | |''',
        ''' -----
              o |
             /|\|
              | |
              | |''',
        ''' -----
              o |
             /|\|
              | |
             /| |''',
        ''' -----
              o |
             /|\|
              | |
             /|\|''']

def chooseWord(word):
    i=random.randint(0,len(word)-1)
    new_word=word[i]
    return new_word

def displayBoard(missedLetters, correctLetters, secretWord):
    blanks = "_" * len(secretWord)
    for letter in missedLetters:
        print(hangman_fig[len(missedLetters)])
        print("missed letter: ")
        print(letter)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks=blanks[:i]+secretWord[i]+blanks[i+1:]

    for char in blanks:
        print(char, end=" ")

def getGuess (alreadyGuessed):
    while True:
        print("Guess a letter: ")
        guess=input()
        guess=guess.lower()
        if len(guess)!=1:
            print("Please enter a letter.")
        elif guess in alreadyGuessed:
            print("You have already guessed that letter, choose again")
        else: return guess

def playAgain():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')

print('HANGMAN')
missedLetters=""
correctWord=""
secretWord=chooseWord(secret_words)
gameIsDone=False
foundAllLetters=False
while True:
    displayBoard(missedLetters,correctWord,secretWord)
    guess=getGuess(missedLetters+correctWord)

    if guess in secretWord:
        correctWord=correctWord+guess
        foundAllLetters=True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctWord:
                foundAllLetters=False
                break
    if foundAllLetters:
        print('YES! The secret word is "'+secretWord+'" You have won!')
        gameIsDone=True
    else:
        missedLetters=missedLetters+guess

    if len(missedLetters)==len(hangman_fig)-1:
        print("You have run out of guesses. ", 'The word was "'+secretWord+'"')
        gameIsDone=True

    if gameIsDone:
        if playAgain():
            missedLetters=''
            correctWord=''
            gameIsDone=False
            secretWord=chooseWord(secret_words)
        else:
            break
