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
    try:
        with open(self.filename, 'r') as fhand:
            for line in fhand:
                word = line.rstrip()
                words[word] = word

    except OSError as e:
        print(f"Error writing to file: {e}")

    return words

  # JSON file
  def readWords(self):
    with open(self.filename, 'r') as fhand:
      words = json.load(fhand)
    return words

class EntropySolver:
  def __init__(self):
    # Read words
    self.fileReader = FileLoader('words.txt', 'txt')
    self.wordList = self.fileReader.wordList
    # Init guess list to all possible words
    self.guessList = self.fileReader.wordList

  # Creates sequence for guess and answer
  # Accepts two strings, returns array of enums
  def check(self, guess: str, answer: str) -> list[Guess]:
    verify = []

    # Count number of duplicate letters in answer
    num_letters = {}
    for i in range(len(answer)):
       if answer[i] not in num_letters:
          num_letters[answer[i]] = 1
       else:
        num_letters[answer[i]] = num_letters[answer[i]] + 1

    for i in range(len(answer)):
        if guess[i] == answer[i]:
            verify.append(Guess.GREEN)
            num_letters[guess[i]] = num_letters[guess[i]] - 1
        elif guess[i] in answer and num_letters[guess[i]] > 0: # Letter in word and same number of letters are in word
            verify.append(Guess.YELLOW)
            num_letters[guess[i]] = num_letters[guess[i]] - 1
        else:
            verify.append(Guess.GRAY)
    return verify
    
  # Reduces guess list based on guess and verify info
  # guess: string
  # verify: Guess enum array
  def reduce(self, guess: str, verify: list[Guess]):
    newCodes = {}
    for answer in self.guessList:
      if self.check(guess, answer) == verify:
        newCodes[answer] = answer
    self.guessList = newCodes

  # Returns highest entropy next guess
  # Based on current guess and verify info
  def distribution(self, guess: str, verify: list[Guess]) -> dict[float, str]:
    # Reduce possible guesses
    self.reduce(guess, verify)
    # TODO: What if two values with same entropy?

    # TODO: Better error handling?
    if len(self.guessList) == 0:
      print("No valid guess")
      return

    # Sort based on entropy
    possible_guesses = {}
    for answer in self.guessList:
      scores = {}
      for guess in self.guessList:
        score = tuple(self.check(guess, answer))
        if score not in scores:
          scores[score] = 1
        else:
          scores[score] += 1

      ent = self.entropy(scores)
      possible_guesses[ent] = answer

    # Sort based on entropy
    possible_guesses = dict(sorted(possible_guesses.items()))
    
    return possible_guesses

  def entropy(self, dictionary):
    total = sum(dictionary.values())
    ent = 0
    for item in dictionary.values():
      p = item/total
      ent -= p * log(p,2)
    return ent
