from tkinter import *


class MyApp:
    def __init__(self, myParent):
        self.container1 = Frame(myParent)
        self.container1.pack()

        self.botao1 = Button(self.container1)
        self.botao1['text'] = 'Hello World!'
        self.botao1['background'] = 'gray'
        self.botao1.pack()

        self.button2 = Button(self.container1)
        self.button2.configure(text="Off to join the circus!")
        self.button2.configure(background="tan")
        self.button2.pack()

        self.button3 = Button(self.container1)
        self.button3.configure(text="Join me?", background="cyan")
        self.button3.pack()

        self.button4 = Button(self.container1, text="Goodbye!",
                              background="red")
        self.button4.pack()


root = Tk()
myapp = MyApp(root)
root.mainloop()

