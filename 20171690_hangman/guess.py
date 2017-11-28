class Guess:
    def __init__(self, word):
        self.secretWord = word
        self.wordset = set(word)
        self.guessedChars = set()
        self.numTries = 0
        
    def display(self):
        self.currentStatus = ''
        for i in self.secretWord:
            if(i in self.guessedChars):
                self.currentStatus += i
            else:
                self.currentStatus += '_'
        print(self.currentStatus)
        print('Tries :', self.numTries)

    def guess(self, character):
        self.guessedChars.add(character)
        if(character not in self.secretWord):
            self.numTries += 1
        if(self.wordset == (self.wordset & self.guessedChars)):
            return True
        else:
            return False
            
            
