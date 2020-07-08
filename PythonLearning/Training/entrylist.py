from tkinter import *

root = Tk()

def command():
    lista = list()
    e1 = int(entry1.get())
    e2 = int(entry2.get())
    lista = [e1, e2]
    entry3.insert(0, sum(lista))


entry1 = Entry(root)
entry2 = Entry(root)
button = Button(root, text="Print", command=command)
entry3 = Entry(root)


entry1.pack()
entry2.pack()
button.pack()
entry3.pack()

root.mainloop()
