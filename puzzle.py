class puzzle():
    def __init__(self, w):
        self.answer = w.upper()
        self.word = [letter.capitalize() for letter in w] 
        self.revealed = [''] * len(w) # This will turn the letters into a length and apply the same amount of empty strings
                                      # will be filled w/ correct guesses
        self.missed = 0
        self.gameOver = False
        self.won = False
        self.chose = []

    def canGuessLetter(self, guess):
        if guess not in self.chose:
            return True 
        else:
            return False

    def checkLetter(self, letter):
        self.chose.append(letter)
        
        # print('Chosen letters:', self.chose) - debug
        
        if letter in self.word:
            
            # print('Correct guess:', letter) - debug
            
            return True
        else:
            
            # print('Incorrect guess:', letter) - debug
            
            return False
    
    def miss(self):
        self.missed += 1
        
        print('Number of missed guesses:', self.missed) # This was not printing when running the code before adding p.miss() on line 38 in the game file. 
                                                        # Nice debug catch that I'm going to turn into a feature. It's nice to see how many live you have left. 
        if self.missed > 5:                             # It also works properly and does not count a miss when a repeat letter is entered. 
            self.gameOver = True

    def reveal(self, guessed_letter):
        for i in range(len(self.word)): # Did a lot of googling for this. My understanding is that range() will 'set a value' - See Bib 1
            if self.word[i] == guessed_letter: # for the letters in the list. Much easier than searching for the letters individually.
                self.revealed[i] = guessed_letter
                
                # print('Revealed letters:', self.revealed) - debug
            
            if self.revealed == self.word: # This is the win condition. If the revealed letters == the word chosen
                self.won = True  # Then self.won is switched from False -> True                       

    def printChosen(self, out):
        out == ''
        for letter in self.chose:
            out += letter + ''
        return out

    def printRevealed(self): # I originally had 'out' as an argument here. Because of that, I was getting a TypeError if I won the game. Removing it seems to have done the trick. 
        out = ''
        for letter in self.revealed:
            if letter == '':
                out += '_'
            else:
                out += letter
        return out
        

# Bibliography 1 - https://www.w3schools.com/python/ref_func_range.asp