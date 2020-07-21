from tkinter import *
listaproduto = []
listapeso = []


def command():
    listaproduto.clear()
    listapeso.clear()
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

    somaentry.delete(0, END)
    somaentry.insert(0, sum(listapeso))


def calculo():
    volume = 12000
    if chok.get() is True:
        volume = 9000
    elif chno.get() is True:
        volume = 12000

    rprod1.insert(0, prod1.get())
    rprod2.insert(0, prod2.get())
    rprod3.insert(0, prod3.get())
    rprod4.insert(0, prod4.get())
    rprod5.insert(0, prod5.get())
    rprod6.insert(0, prod6.get())
    rprod7.insert(0, prod7.get())
    rprod8.insert(0, prod8.get())
    rprod9.insert(0, prod9.get())
    rprod10.insert(0, prod10.get())

    tons = int(ton.get())*1000
    pextra = int(pesextra.get())
    ptotbat = 0
    for btl in range(1, 51):
        batid = (tons + pextra)/btl
        if batid < volume:
            ptotbat = int(batid)
            bat.delete(0, END)
            bat.insert(0, btl)

            ptot.delete(0, END)
            ptot.insert(0, ptotbat)

            break
    for c, v in enumerate(listapeso):
        if c == 0:
            peso1final = v * ptotbat/1000
            peso1int = int(peso1final)
            rpes1.insert(0, peso1int)
        elif c == 1:
            peso2final = v * ptotbat / 1000
            peso2int = int(peso2final)
            rpes2.insert(0, peso2int)
        elif c == 2:
            peso3final = v * ptotbat / 1000
            peso3int = int(peso3final)
            rpes3.insert(0, peso3int)
        elif c == 3:
            peso4final = v * ptotbat / 1000
            peso4int = int(peso4final)
            rpes4.insert(0, peso4int)
        elif c == 4:
            peso5final = v * ptotbat / 1000
            peso5int = int(peso5final)
            rpes5.insert(0, peso5int)
        elif c == 5:
            peso6final = v * ptotbat / 1000
            peso6int = int(peso6final)
            rpes6.insert(0, peso6int)
        elif c == 6:
            peso7final = v * ptotbat / 1000
            peso7int = int(peso7final)
            rpes7.insert(0, peso7int)
        elif c == 7:
            peso8final = v * ptotbat / 1000
            peso8int = int(peso8final)
            rpes8.insert(0, peso8int)
        elif c == 8:
            peso9final = v * ptotbat / 1000
            peso9int = int(peso9final)
            rpes9.insert(0, peso9int)
        elif c == 9:
            peso10final = v * ptotbat / 1000
            peso10int = int(peso10final)
            rpes10.insert(0, peso10int)


janela = Tk()
xx = 30
yy = 20


myprods = []
mypesos = []


for i in range(0, 19, 2):
    if i == 0:
        labelprod1 = Label(janela, text='Produto 1:')
        labelprod1.grid(row=i, column=0, pady=1)
        prod1 = Entry(janela)
        prod1.grid(row=i, column=1, pady=1, padx=5)
        labelpeso1 = Label(janela, text='Peso:')
        labelpeso1.grid(row=i + 1, column=0, pady=1)
        pes1 = Entry(janela)
        pes1.grid(row=i + 1, column=1, pady=1, padx=5)

    elif i == 2:
        labelprod2 = Label(janela, text='Produto 2:')
        labelprod2.grid(row=i, column=0, pady=1)
        prod2 = Entry(janela)
        prod2.grid(row=i, column=1, pady=1, padx=5)
        labelpeso2 = Label(janela, text='Peso:')
        labelpeso2.grid(row=i + 1, column=0, pady=1)
        pes2 = Entry(janela)
        pes2.grid(row=i + 1, column=1, pady=1, padx=5)
    elif i == 4:
        labelprod3 = Label(janela, text='Produto 3:')
        labelprod3.grid(row=i, column=0, pady=1)
        prod3 = Entry(janela)
        prod3.grid(row=i, column=1, pady=1, padx=5)
        labelpeso3 = Label(janela, text='Peso:')
        labelpeso3.grid(row=i + 1, column=0, pady=1)
        pes3 = Entry(janela)
        pes3.grid(row=i + 1, column=1, pady=1, padx=5)
    elif i == 6:
        labelprod4 = Label(janela, text='Produto 4:')
        labelprod4.grid(row=i, column=0, pady=1)
        prod4 = Entry(janela)
        prod4.grid(row=i, column=1, pady=1, padx=5)
        labelpeso4 = Label(janela, text='Peso:')
        labelpeso4.grid(row=i + 1, column=0, pady=1)
        pes4 = Entry(janela)
        pes4.grid(row=i + 1, column=1, pady=1, padx=5)
    elif i == 8:
        labelprod5 = Label(janela, text='Produto 5:')
        labelprod5.grid(row=i, column=0, pady=1)
        prod5 = Entry(janela)
        prod5.grid(row=i, column=1, pady=1, padx=5)
        labelpeso5 = Label(janela, text='Peso:')
        labelpeso5.grid(row=i + 1, column=0, pady=1)
        pes5 = Entry(janela)
        pes5.grid(row=i + 1, column=1, pady=1, padx=5)
    elif i == 10:
        labelprod6 = Label(janela, text='Produto 6:')
        labelprod6.grid(row=i, column=0, pady=1)
        prod6 = Entry(janela)
        prod6.grid(row=i, column=1, pady=1, padx=5)
        labelpeso6 = Label(janela, text='Peso:')
        labelpeso6.grid(row=i + 1, column=0, pady=1)
        pes6 = Entry(janela)
        pes6.grid(row=i + 1, column=1, pady=1, padx=5)
    elif i == 12:
        labelprod7 = Label(janela, text='Produto 7:')
        labelprod7.grid(row=i, column=0, pady=1)
        prod7 = Entry(janela)
        prod7.grid(row=i, column=1, pady=1, padx=5)
        labelpeso7 = Label(janela, text='Peso:')
        labelpeso7.grid(row=i + 1, column=0, pady=1)
        pes7 = Entry(janela)
        pes7.grid(row=i + 1, column=1, pady=1, padx=5)
    elif i == 14:
        labelprod8 = Label(janela, text='Produto 8:')
        labelprod8.grid(row=i, column=0, pady=1)
        prod8 = Entry(janela)
        prod8.grid(row=i, column=1, pady=1, padx=5)
        labelpeso8 = Label(janela, text='Peso:')
        labelpeso8.grid(row=i + 1, column=0, pady=1)
        pes8 = Entry(janela)
        pes8.grid(row=i + 1, column=1, pady=1, padx=5)
    elif i == 16:
        labelprod9 = Label(janela, text='Produto 9:')
        labelprod9.grid(row=i, column=0, pady=1)
        prod9 = Entry(janela)
        prod9.grid(row=i, column=1, pady=1, padx=5)
        labelpeso9 = Label(janela, text='Peso:')
        labelpeso9.grid(row=i + 1, column=0, pady=1)
        pes9 = Entry(janela)
        pes9.grid(row=i + 1, column=1, pady=1, padx=5)
    elif i == 18:
        labelprod10 = Label(janela, text='Produto 10:')
        labelprod10.grid(row=i, column=0, pady=1)
        prod10 = Entry(janela)
        prod10.grid(row=i, column=1, pady=1, padx=5)
        labelpeso10 = Label(janela, text='Peso:')
        labelpeso10.grid(row=i + 1, column=0, pady=1)
        pes10 = Entry(janela)
        pes10.grid(row=i + 1, column=1, pady=1, padx=5)

labelnone1 = Label(janela)
labelnone1.grid(row=20, column=0, padx=1, pady=2)
botao = Button(janela, text="Salvar!", command=command)
botao.grid(row=21, column=1, ipadx=10, ipady=2)

labelnone2 = Label(janela)
labelnone2.grid(row=23, column=0, padx=1, pady=2)
somalabel = Label(janela, text='SOMA:')
somalabel.grid(row=25, column=0)
somaentry = Entry(janela)
somaentry.grid(row=25, column=1)

labelnone3 = Label(janela)
labelnone3.grid(row=1, column=2, padx=20, pady=1)
labeltonelada = Label(janela, text='Toneladas: (Ex: 32)')
labeltonelada.grid(row=1, column=10, pady=2)
ton = Entry(janela)
ton.grid(row=3, column=10, pady=1, padx=5)

labelvolume = Label(janela, text='Volume: (Uréia/Nitrogenado)')
labelvolume.grid(row=5, column=10, pady=2)
chok = BooleanVar()
chno = BooleanVar()
chok.set(False)
chno.set(False)

cbyes = Checkbutton(janela, text='Sim', var=chok)
cbyes.grid(row=6, column=10, pady=1, padx=1)

cbno = Checkbutton(janela, text='Não', var=chno)
cbno.grid(row=7, column=10, pady=1, padx=1)

labelpextra = Label(janela, text='Peso Extra:')
labelpextra.grid(row=10, column=10, pady=1, padx=1)
pesextra = Entry(janela)
pesextra.grid(row=11, column=10, pady=1, padx=5)

botaoprincipal = Button(janela, text='PRONTO!', command=calculo, height=0, width=10)
botaoprincipal.grid(row=15, column=10, pady=0, padx=1)

labelnone4 = Label(janela)
labelnone4.grid(row=0, column=20, padx=50, pady=1)
labelidprod = Label(janela, text='Produto')
labelidprod.grid(row=0, column=25, pady=1, padx=1)
labelidpeso = Label(janela, text='Peso')
labelidpeso.grid(row=0, column=26, pady=1, padx=1)

for i in range(1, 21, 2):
    if i == 1:
        rprod1 = Entry(janela)
        rprod1.grid(row=i, column=25, pady=1)
        rpes1 = Entry(janela)
        rpes1.grid(row=i, column=26, pady=1, padx=5)

    elif i == 3:
        rprod2 = Entry(janela)
        rprod2.grid(row=i, column=25, pady=1)
        rpes2 = Entry(janela)
        rpes2.grid(row=i, column=26, pady=1, padx=5)

    elif i == 5:
        rprod3 = Entry(janela)
        rprod3.grid(row=i, column=25, pady=1)
        rpes3 = Entry(janela)
        rpes3.grid(row=i, column=26, pady=1, padx=5)

    elif i == 7:
        rprod4 = Entry(janela)
        rprod4.grid(row=i, column=25, pady=1)
        rpes4 = Entry(janela)
        rpes4.grid(row=i, column=26, pady=1, padx=5)

    elif i == 9:
        rprod5 = Entry(janela)
        rprod5.grid(row=i, column=25, pady=1)
        rpes5 = Entry(janela)
        rpes5.grid(row=i, column=26, pady=1, padx=5)

    elif i == 11:
        rprod6 = Entry(janela)
        rprod6.grid(row=i, column=25, pady=1)
        rpes6 = Entry(janela)
        rpes6.grid(row=i, column=26, pady=1, padx=5)

    elif i == 13:
        rprod7 = Entry(janela)
        rprod7.grid(row=i, column=25, pady=1)
        rpes7 = Entry(janela)
        rpes7.grid(row=i, column=26, pady=1, padx=5)

    elif i == 15:
        rprod8 = Entry(janela)
        rprod8.grid(row=i, column=25, pady=1)
        rpes8 = Entry(janela)
        rpes8.grid(row=i, column=26, pady=1, padx=5)

    elif i == 17:
        rprod9 = Entry(janela)
        rprod9.grid(row=i, column=25, pady=1)
        rpes9 = Entry(janela)
        rpes9.grid(row=i, column=26, pady=1, padx=5)

    elif i == 19:
        rprod10 = Entry(janela)
        rprod10.grid(row=i, column=25, pady=1)
        rpes10 = Entry(janela)
        rpes10.grid(row=i, column=26, pady=1, padx=5)

labelnone5 = Label(janela)
labelnone5.grid(row=20, column=25, padx=1, pady=1)
batlabel = Label(janela, text='Batidas:')
batlabel.grid(row=23, column=25, pady=1, padx=1)
bat = Entry(janela)
bat.grid(row=25, column=25, pady=1, padx=1)

labelnone6 = Label(janela)
labelnone6.grid(row=20, column=26, padx=1, pady=1)
ptotlabel = Label(janela, text='Peso Total:')
ptotlabel.grid(row=23, column=26, pady=1, padx=1)
ptot = Entry(janela)
ptot.grid(row=25, column=26, pady=1, padx=1)


janela.geometry('800x600+500+500')
janela.title('Auto Fomula M1')
janela.mainloop()
