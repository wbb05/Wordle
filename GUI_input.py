from tkinter import *
from tkinter import ttk

from Wordle import EntropySolver
from Wordle import Guess
from Wordle import Wordle

class GUI:

    def __init__(self, root):

        # Wordle game
        self.Game = Wordle()
        self.Solver = EntropySolver(self.Game)

        # Make GUI
        root.title("Wordle Solver")

        # Add grid
        mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # Add input fields
        self.first_letter = StringVar()
        self.second_letter = StringVar()
        self.third_letter = StringVar()
        self.fourth_letter = StringVar()
        self.fifth_letter = StringVar()

        first_letter_combobox = ttk.Combobox(mainframe, textvariable=self.first_letter)
        first_letter_combobox['values'] = ('Green', 'Yellow', 'Gray')
        first_letter_combobox.grid(column = 1, row = 1, sticky = (W,E))

        second_letter_combobox = ttk.Combobox(mainframe, textvariable=self.second_letter)
        second_letter_combobox['values'] = ('Green', 'Yellow', 'Gray')
        second_letter_combobox.grid(column = 2, row = 1, sticky = (W,E))

        third_letter_combobox = ttk.Combobox(mainframe, textvariable=self.third_letter)
        third_letter_combobox['values'] = ('Green', 'Yellow', 'Gray')
        third_letter_combobox.grid(column = 3, row = 1, sticky = (W,E))

        fourth_letter_combobox = ttk.Combobox(mainframe, textvariable=self.fourth_letter)
        fourth_letter_combobox['values'] = ('Green', 'Yellow', 'Gray')
        fourth_letter_combobox.grid(column = 5, row = 1, sticky = (W,E))

        fifth_letter_combobox = ttk.Combobox(mainframe, textvariable=self.fifth_letter)
        fifth_letter_combobox['values'] = ('Green', 'Yellow', 'Gray')
        fifth_letter_combobox.grid(column = 6, row = 1, sticky = (W,E))

        
        # Add button to calculate guess
        enter_button = ttk.Button(mainframe, text= "Enter", command= self.enter_letters)
        enter_button.grid(column = 1, row = 2, sticky = (W,E))

        # Add labels to show guesses
        # First guess is always tares?
        self.guess1 = StringVar()
        self.guess1.set('Slate')
        self.guess2 = StringVar()
        self.guess3 = StringVar()
        self.guess4 = StringVar()
        self.guess5 = StringVar()
        self.guess6 = StringVar()

        # Array of guesses for easy access
        self.guesses = [self.guess1, self.guess2, self.guess3, self.guess4, self.guess5, self.guess6]
        self.guess_idx = 0

        ttk.Label(mainframe, textvariable= self.guess1).grid(column=1, row=3, sticky=W)
        ttk.Label(mainframe, textvariable= self.guess2).grid(column=1, row=4, sticky=W)
        ttk.Label(mainframe, textvariable= self.guess3).grid(column=1, row=5, sticky=W)
        ttk.Label(mainframe, textvariable= self.guess4).grid(column=1, row=6, sticky=W)
        ttk.Label(mainframe, textvariable= self.guess5).grid(column=1, row=7, sticky=W)
        ttk.Label(mainframe, textvariable= self.guess6).grid(column=1, row=8, sticky=W)

        # Add button to reset game
        reset_button = ttk.Button(mainframe, text= "Reset", command= self.reset_game)
        reset_button.grid(column= 3, row = 2, sticky= (W,E))


    def enter_letters(self):
        # Convert inputted letters
        letters = [self.convert_letter(self.first_letter.get()), self.convert_letter(self.second_letter.get()),
                   self.convert_letter(self.third_letter.get()), self.convert_letter(self.fourth_letter.get()),
                   self.convert_letter(self.fifth_letter.get())]

        # Get current guess
        curr_guess = self.guesses[self.guess_idx].get()

        # Reduce based on inputted letters
        self.Solver.reduce(curr_guess, letters)

        next_guess = self.Solver.distribution()

        self.guess_idx += 1
        self.guesses[self.guess_idx].set(next_guess)

    # Converts text variables to enum variables
    # Returns array of converted variables
    def convert_letter(self, letter):
            
        if letter == "Green":
            return Guess.GREEN
        elif letter == "Yellow":
            return Guess.YELLOW
        elif letter == "Gray":
            return Guess.GRAY
        else:
            # TODO: Proper error handling
            print("ERROR: Letter is empty")
            return

    def reset_game(self):

        # Reset labels
        self.guess1.set('Slate')
        self.guess2.set('')
        self.guess3.set('')
        self.guess4.set('')
        self.guess5.set('')
        self.guess6.set('')

        # Array of guesses for easy access
        self.guesses = [self.guess1, self.guess2, self.guess3, self.guess4, self.guess5, self.guess6]
        self.guess_idx = 0

        # Reset solver
        self.Solver = EntropySolver(self.Game)

            
        


        
        
        
        


        