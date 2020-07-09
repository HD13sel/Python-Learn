from tkinter import *


def command():
    listaproduto = []
    listapeso = []
    for ep in entryprod:
        listaproduto = listaproduto.append(ep)
    for pes in entrypeso:
        listapeso = listapeso.append(pes)

    print(listaproduto)
    print(listapeso)


janela = Tk()
xx = 30
yy = 20

myprods = []
mypesos = []


for i in range(1, 21, 2):
    labelprod = Label(janela, text=f'Produto {(i/2)-1:.0f}:')
    labelprod.grid(row=i, column=0, pady=1)
    labelpeso = Label(janela, text='Peso:')
    labelpeso.grid(row=i+1, column=0, pady=1)
    if i == 0:
        prod1 = Entry(janela)
        prod1.grid(row=i, column=1, pady=1, padx=5)
    entrypeso = Entry(janela)
    entrypeso.grid(row=i+1, column=1, pady=1, padx=5)


botao = Button(janela, text="Salvar!", command=command)
botao.grid(row=30, column=1, ipadx=5, ipady=5)


janela.geometry('800x600+500+500')
janela.mainloop()
