import Wordle
import GUI_input
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

