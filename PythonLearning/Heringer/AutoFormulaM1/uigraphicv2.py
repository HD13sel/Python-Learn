from tkinter import *


def command():
    listaproduto = []
    listapeso = []
    for e in range(1, 11):
        if e == 1:
            listaproduto.append(prod1.get())
            if pes1.get() == '':
                peso1 = 0
            else:
                peso1 = int(pes1.get())
            listapeso.append(peso1)
        elif e == 2:
            listaproduto.append(prod2.get())
            if pes2.get() == '':
                peso2 = 0
            else:
                peso2 = int(pes2.get())
            listapeso.append(peso2)
        elif e == 3:
            listaproduto.append(prod3.get())
            if pes3.get() == '':
                peso3 = 0
            else:
                peso3 = int(pes3.get())
            listapeso.append(peso3)
        elif e == 4:
            listaproduto.append(prod4.get())
            if pes4.get() == '':
                peso4 = 0
            else:
                peso4 = int(pes4.get())
            listapeso.append(peso4)
        elif e == 5:
            listaproduto.append(prod5.get())
            if pes5.get() == '':
                peso5 = 0
            else:
                peso5 = int(pes5.get())
            listapeso.append(peso5)
        elif e == 6:
            listaproduto.append(prod6.get())
            if pes6.get() == '':
                peso6 = 0
            else:
                peso6 = int(pes6.get())
            listapeso.append(peso6)
        elif e == 7:
            listaproduto.append(prod7.get())
            if pes7.get() == '':
                peso7 = 0
            else:
                peso7 = int(pes7.get())
            listapeso.append(peso7)
        elif e == 8:
            listaproduto.append(prod8.get())
            if pes8.get() == '':
                peso8 = 0
            else:
                peso8 = int(pes8.get())
            listapeso.append(peso8)
        elif e == 9:
            listaproduto.append(prod9.get())
            if pes9.get() == '':
                peso9 = 0
            else:
                peso9 = int(pes9.get())
            listapeso.append(peso9)
        elif e == 10:
            listaproduto.append(prod10.get())
            if pes10.get() == '':
                peso10 = 0
            else:
                peso10 = int(pes10.get())
            listapeso.append(peso10)

    somaentry.insert(0, sum(listapeso))


janela = Tk()
xx = 30
yy = 20

myprods = []
mypesos = []


for i in range(0, 19, 2):
    if i == 0:
        labelprod1 = Label(janela, text='Produto 1')
        labelprod1.grid(row=i, column=0, pady=1)
        prod1 = Entry(janela)
        prod1.grid(row=i, column=1, pady=1, padx=5)
        labelpeso1 = Label(janela, text='Peso:')
        labelpeso1.grid(row=i + 1, column=0, pady=1)
        pes1 = Entry(janela)
        pes1.grid(row=i + 1, column=1, pady=1, padx=5)

    elif i == 2:
        labelprod2 = Label(janela, text='Produto 2')
        labelprod2.grid(row=i, column=0, pady=1)
        prod2 = Entry(janela)
        prod2.grid(row=i, column=1, pady=1, padx=5)
        labelpeso2 = Label(janela, text='Peso:')
        labelpeso2.grid(row=i + 1, column=0, pady=1)
        pes2 = Entry(janela)
        pes2.grid(row=i + 1, column=1, pady=1, padx=5)
    elif i == 4:
        labelprod3 = Label(janela, text='Produto 3')
        labelprod3.grid(row=i, column=0, pady=1)
        prod3 = Entry(janela)
        prod3.grid(row=i, column=1, pady=1, padx=5)
        labelpeso3 = Label(janela, text='Peso:')
        labelpeso3.grid(row=i + 1, column=0, pady=1)
        pes3 = Entry(janela)
        pes3.grid(row=i + 1, column=1, pady=1, padx=5)
    elif i == 6:
        labelprod4 = Label(janela, text='Produto 4')
        labelprod4.grid(row=i, column=0, pady=1)
        prod4 = Entry(janela)
        prod4.grid(row=i, column=1, pady=1, padx=5)
        labelpeso4 = Label(janela, text='Peso:')
        labelpeso4.grid(row=i + 1, column=0, pady=1)
        pes4 = Entry(janela)
        pes4.grid(row=i + 1, column=1, pady=1, padx=5)
    elif i == 8:
        labelprod5 = Label(janela, text='Produto 5')
        labelprod5.grid(row=i, column=0, pady=1)
        prod5 = Entry(janela)
        prod5.grid(row=i, column=1, pady=1, padx=5)
        labelpeso5 = Label(janela, text='Peso:')
        labelpeso5.grid(row=i + 1, column=0, pady=1)
        pes5 = Entry(janela)
        pes5.grid(row=i + 1, column=1, pady=1, padx=5)
    elif i == 10:
        labelprod6 = Label(janela, text='Produto 6')
        labelprod6.grid(row=i, column=0, pady=1)
        prod6 = Entry(janela)
        prod6.grid(row=i, column=1, pady=1, padx=5)
        labelpeso6 = Label(janela, text='Peso:')
        labelpeso6.grid(row=i + 1, column=0, pady=1)
        pes6 = Entry(janela)
        pes6.grid(row=i + 1, column=1, pady=1, padx=5)
    elif i == 12:
        labelprod7 = Label(janela, text='Produto 7')
        labelprod7.grid(row=i, column=0, pady=1)
        prod7 = Entry(janela)
        prod7.grid(row=i, column=1, pady=1, padx=5)
        labelpeso7 = Label(janela, text='Peso:')
        labelpeso7.grid(row=i + 1, column=0, pady=1)
        pes7 = Entry(janela)
        pes7.grid(row=i + 1, column=1, pady=1, padx=5)
    elif i == 14:
        labelprod8 = Label(janela, text='Produto 8')
        labelprod8.grid(row=i, column=0, pady=1)
        prod8 = Entry(janela)
        prod8.grid(row=i, column=1, pady=1, padx=5)
        labelpeso8 = Label(janela, text='Peso:')
        labelpeso8.grid(row=i + 1, column=0, pady=1)
        pes8 = Entry(janela)
        pes8.grid(row=i + 1, column=1, pady=1, padx=5)
    elif i == 16:
        labelprod9 = Label(janela, text='Produto 9')
        labelprod9.grid(row=i, column=0, pady=1)
        prod9 = Entry(janela)
        prod9.grid(row=i, column=1, pady=1, padx=5)
        labelpeso9 = Label(janela, text='Peso:')
        labelpeso9.grid(row=i + 1, column=0, pady=1)
        pes9 = Entry(janela)
        pes9.grid(row=i + 1, column=1, pady=1, padx=5)
    elif i == 18:
        labelprod10 = Label(janela, text='Produto 10')
        labelprod10.grid(row=i, column=0, pady=1)
        prod10 = Entry(janela)
        prod10.grid(row=i, column=1, pady=1, padx=5)
        labelpeso10 = Label(janela, text='Peso:')
        labelpeso10.grid(row=i + 1, column=0, pady=1)
        pes10 = Entry(janela)
        pes10.grid(row=i + 1, column=1, pady=1, padx=5)


botao = Button(janela, text="Salvar!", command=command)
botao.grid(row=30, column=1, ipadx=5, ipady=5)
somalabel = Label(janela, text='SOMA:')
somalabel.grid(row=33, column=0)
somaentry = Entry(janela)
somaentry.grid(row=33, column=1)
labeltonelada = Label(janela, text='Toneladas')
labeltonelada.grid(row=1, column=10, pady=1)
ton = Entry(janela)
ton.grid(row=3, column=10, pady=1, padx=5)


janela.geometry('800x600+500+500')
janela.mainloop()
