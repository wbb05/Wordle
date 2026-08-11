from tkinter import *
from tkinter import ttk

class Wordle_GUI:

    def __init__(self, root):

        # Add title
        root.title("Wordle Player")

        # Add grid
        mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # Add entry for guess
        self.guess = StringVar()
        guess_entry = ttk.Entry(mainframe, width=7, textvariable=self.guess)
        guess_entry.grid(column=1, row=4, sticky=(W, E))

        # Add label for guess
        ttk.Label(mainframe, text="Enter Guess").grid(column=1, row=3, sticky=E)

        # Add button to enter guess
        ttk.Button(mainframe, text= "Enter", command=self.add_guess).grid(column = 1, row = 6, sticky= W)

        # Add labels to record guesses
        self.guess1 = StringVar()
        self.guess2 = StringVar()
        self.guess3 = StringVar()
        self.guess4 = StringVar()
        self.guess5 = StringVar()

        ttk.Label(mainframe, textvariable= self.guess1).grid(column = 2, row = 1, sticky = (W,E))
        ttk.Label(mainframe, textvariable= self.guess2).grid(column = 2, row = 2, sticky = (W,E))
        ttk.Label(mainframe, textvariable= self.guess3).grid(column = 2, row = 3, sticky = (W,E))
        ttk.Label(mainframe, textvariable= self.guess4).grid(column = 2, row = 4, sticky = (W,E))
        ttk.Label(mainframe, textvariable= self.guess5).grid(column = 2, row = 5, sticky = (W,E))

        # Current number of guesses
        self.num_guesses = 0

    def add_guess(self):
        # For now, just switch case, not loop
        self.num_guesses += 1

        match self.num_guesses:
            case 1:
                self.guess1.set(self.guess.get())
            case 2:
                self.guess2.set(self.guess.get())
            case 3:
                self.guess3.set(self.guess.get())
            case 4:
                self.guess4.set(self.guess.get())
            case 5:
                self.guess5.set(self.guess.get())
        