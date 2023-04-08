from puzzle import puzzle
from random import randint

with open("words.txt", 'r') as listWords: 
    wordList = [word.rstrip('\n') for word in listWords]
    
    # print(wordList) debug

# Game loop

while True:
    wordIndex = randint(0, len(wordList) - 1)
    p = puzzle(wordList[wordIndex]) # p represents an instance of the game. Most important variable 
    break

# Puzzle loop

while True:
    
    print(p.printRevealed())
    print('Chosen letters: ' + p.printChosen(''))

    guess = input('Please guess a letter: ').upper() # Convert entries into uppercase
    
    if guess == '':
       guess = input('The entry was blank. Please enter a letter: ').upper() # Still need to convert this to uppercase. Otherwise that entry will be as the user entered it. 
    # ^ Prevents blank entry

    if guess.isnumeric():
        guess = input('You have entered a number. Please enter a letter: ').upper() # need upper()
    # ^ prevents numeric entry

    if not p.canGuessLetter(guess):
        print('You have already guessed that letter. Please guess again.')
        continue

    if p.checkLetter(guess):
        p.reveal(guess)
        print('Good choice!')
    else:
        p.miss() # Didn't originally have this here, need it so that the game will end after 6 misses
        print('Oops!')

    if p.gameOver:
        print('You are out of lives and lost! The word was:', p.answer) # Need to make it it's own statment. Was getting a type error since I was initially trying 
                                                                        # to include this with the play again input below. 
        play_again_loss = input('Would you like to play again? (Y/N): ').upper()
        
        if play_again_loss == 'Y':
            p = puzzle(wordList[randint(0, len(wordList) - 1)])
        elif play_again_loss != 'Y' or 'N':
            play_again_loss2 = input('That is not a valid input. Would you like to play again? (Y/N): ').upper()
        else:  # ^ Need a new variable for blank/misentries at the play again input. 
            break

        if play_again_loss2 == 'Y': # This accounts for blank/misentries in the play again feature. 
            p = puzzle(wordList[randint(0, len(wordList) - 1)])
        else:
            break

    if p.won:
        print('Congratulations, you win! The word was: ', p.answer) # I like printing the word on the win. I feel like it looks a little better/is a better experience. 
        
        play_again_win = input('Would you like to play again? (Y/N): ').upper()
        
        if play_again_win == 'Y':
            p = puzzle(wordList[randint(0, len(wordList) - 1)])
        elif play_again_win != 'Y' or 'N':
            play_again_win2 = input('That is not a valid input. Would you like to play again? (Y/N): ').upper()
        else: # ^ Same as loss, need new variable
            break

        if play_again_win2 == 'Y': # This accounts for blank/misentries in the play again feature. 
            p = puzzle(wordList[randint(0, len(wordList) - 1)])
        else:
            break

# Everything appears to be working. I've throughly tested this. 


# This is set up w/ the assumption that the user will follow the instructions. 
# It does work if the user enters numbers and will eventually return a loss,
# but it does not prevent them from doing so nor does it prompt another entry.
# The issue is that blank entries count as a miss. 

# Managed to set it up to account for these inputs. I left the original note in there so you could see my thought process.
# I've added a lot to this lab and really enjoyed it. Sorry for the extra stuff but I had some 
# extra time this week and figured I'd run with it!