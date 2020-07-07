import tkinter as tk


def bt_onclick():
    rp1.delete(0, tk.END)
    rp1.insert(0, p1.get())


produtos = list()

janela = tk.Tk()

p1 = tk.Entry(janela)
p1.place(x=100, y=20)

p2 = tk.Entry(janela)
p2.place(x=100, y=40)

p3 = tk.Entry(janela)
p3.place(x=100, y=60)

produtos.append(p1.get())
produtos.append(p2.get())


bt = tk.Button(janela, width=20, text='OK', command=bt_onclick)
bt.place(x=90, y=100)

rp1 = tk.Entry(janela)
rp1.place(x=100, y=140)

rp2 = tk.Entry(janela)
rp2.place(x=100, y=160)

rp3 = tk.Entry(janela)
rp3.place(x=100, y=180)

janela.geometry('300x300+300+300')
janela.mainloop()
