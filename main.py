import GUI_input
from Wordle import *
from tkinter import Tk

# TODO:
# Error handling?
# Double letters
# Add top five potential guesses
# Add number of guesses

if __name__ == '__main__':
    #game = Wordle.Wordle()
    #game.play()
    #game.aiPlay()

    # Set up GUI
    root = Tk()
    GUI_input.GUI(root)
    root.mainloop()

    # solver = EntropySolver()
    # print(solver.distribution("slate", [Guess.GRAY, Guess.GRAY, Guess.GRAY, Guess.GRAY, Guess.GREEN]).values())


