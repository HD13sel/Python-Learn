import tkinter
from tkinter import ttk

class Test:
    def __init__(self):
        self.root_window = tkinter.Tk()

        #create who goes first variable
        self.who_goes_first = tkinter.StringVar(None, 's')

        #black radio button
        self._who_goes_first_radiobutton = ttk.Radiobutton(
            self.root_window,
            text = 'Sim',
            variable = self.who_goes_first,
            value = 's')
        self._who_goes_first_radiobutton.grid(row=0, column=1)

        #white radio button
        self._who_goes_first_radiobutton = ttk.Radiobutton(
            self.root_window,
            text = 'Nao',
            variable = self.who_goes_first,
            value = 'n')
        self._who_goes_first_radiobutton.grid(row=1, column=1)

    def start(self) -> None:
        self.root_window.mainloop()

if __name__ == '__main__':

    game = Test()
    game.start()
