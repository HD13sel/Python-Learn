from tkinter import *

root = Tk()

def command():
    print(entry.get().split(" "))

entry = Entry(root)
button = Button(root, text="Print", command=command)

entry.pack()
button.pack()

root.mainloop()
