import json
from random import choice
from math import log
from enum import Enum

class Guess(Enum):
  GREEN = 1
  YELLOW = 2
  GRAY = 3

# Loads word list from file
class FileLoader:
  def __init__(self, filename, type):
    self.filename = filename
    if type == 'txt':
      self.wordList = self.readWordList()
    elif type == 'json':
      self.wordList = self.readWords()

  # Text file
  def readWordList(self):
    words = {}
    with open(self.filename, 'r') as fhand:
      for line in fhand:
        line = line.rstrip().split(' ')
        for word in line:
          words[word] = word
    return words

  # JSON file
  def readWords(self):
    with open(self.filename, 'r') as fhand:
      words = json.load(fhand)
    return words

class Wordle:
  def __init__(self):
    self.fileReader = FileLoader('words.txt', 'txt')
    self.wordList = self.fileReader.wordList
    self.answer = choice(list(self.wordList))
    self.AI = EntropySolver(self)
  
  # Get result for AI play
  def user_input(self):
    
     verification =  input('Result: ').split(' ')
     for item in verification:
       if item in ['g', 'G', 'Green', 'green']:
         verification[verification.index(item)] = Guess.GREEN
       elif item in ['y', 'Y', 'Yellow', 'yellow']:
         verification[verification.index(item)] = Guess.YELLOW
       elif item in ['gy', 'GY', 'Gray', 'gray']:
         verification[verification.index(item)] = Guess.GRAY
       else:
          print('Invalid input, try again')
          return self.user_input()
     return verification
  
  # Creates sequence for guess and answer
  # Accepts two strings, returns array of enums
  def check(self, guess: str, answer: str) -> list[Guess]:
    verify = []
    for i in range(len(answer)):
      if guess[i] == answer[i]:
        verify.append(Guess.GREEN)
      elif guess[i] in answer:
        verify.append(Guess.YELLOW)
      else:
        verify.append(Guess.GRAY)
      #answer = answer[:i] + ' ' + answer[i+1:] # For double letters
    return verify

  # Human play
  def play(self):
    for _ in range(6):
      guess = input('Your guess: ')
      verfication = self.check(guess, self.answer)
      print(f'Result: {verfication}')
      if all(item == Guess.GREEN for item in verfication):
        print('You won!!!!!!')
        return

    print(f'You lost! The answer was {self.answer}')

  # Plan:
  # Generate all possible codes
  # Generate all possible guesses
  # Reduce based on check
  # For each code and guess, check and note largest score group
  # Choose guess with minimal score group (maximize entropy)
  def aiPlay(self):
    guess = 'slate'
    for _ in range(6):
      print(f'Computer guess: {guess}')
      verification = self.user_input()
      
      if all(item == Guess.GREEN for item in verification):
        print('You won!!!!!!')
        return
      self.AI.reduce(guess, verification)
      print(f'Number of choices: {len(self.AI.guessList)}')
      
      if (len(self.AI.guessList) <= 5):
        for guess in self.AI.guessList:
          print(f'Possible answer: {guess}')

      guess = self.AI.distribution()
      print(f'Maximum Entropy: {-log(1/len(self.AI.guessList),2)}')
      
    print(f'You lost! The answer was {self.answer}')

  def aiTest(self):
    
    result = []
    for word in self.wordList:
      count = 0
      guess = 'slate'
      self.AI.guessList = self.wordList
      for _ in range(6):
        count += 1
        verification = self.check(guess, word)
        if all(item == 'G' for item in verification):
          result.append(count)
          break

        self.AI.reduce(guess, verification)
        guess = self.AI.distribution()

      if count == 6:
        result.append(count)
    return result

class EntropySolver:
  def __init__(self, game: Wordle):
    self.game = game
    self.guessList = game.wordList
    
  # Reduces guess list based on guess
  # guess: string
  # verify: Guess enum array
  def reduce(self, guess: str, verify: list[Guess]):
    newCodes = {}
    for answer in self.guessList:
      if self.game.check(guess, answer) == verify:
        newCodes[answer] = answer
    self.guessList = newCodes

  # Returns highest entropy next guess
  def distribution(self) -> str:

    # TODO: Better error handling
    if len(self.guessList) == 0:
      print("No valid guess")
      return

    maxx = -1000000
    final = None
    for answer in self.guessList:
      scores = {}
      for guess in self.guessList:
        score = tuple(self.game.check(guess, answer))
        if score not in scores:
          scores[score] = 1
        else:
          scores[score] += 1
      ent = self.entropy(scores)
      if ent > maxx:
        final = answer
        maxx = ent
    print(f'Total Entropy of {final} is {maxx}')
    return final

  def entropy(self, dictionary):
    total = sum(dictionary.values())
    ent = 0
    for item in dictionary.values():
      p = item/total
      ent -= p * log(p,2)
    return ent
  

if __name__ == '__main__':
    game = Wordle()
    #game.play()
    game.aiPlay()
