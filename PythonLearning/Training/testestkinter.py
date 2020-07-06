import tkinter as tk
import tkinter.ttk as ttk


class MenuFormula:
    def __init__(self, master=None):
        # build ui
        # FRAME MENU
        self.menu = ttk.Frame(master)

        # FRAME CADASTRO
        self.cadastro = ttk.Frame(self.menu)

        # FRAME 1
        self.produto1 = ttk.Frame(self.cadastro)
        # LABEL 1
        self.label1 = ttk.Label(self.produto1)
        self.label1.config(text='Produto 1:  ')
        self.label1.pack(side='left')
        # ENTRY 1
        self.prod1 = ttk.Entry(self.produto1)
        self.prod1.pack(side='left')
        # FINALIZANDO FRAME 1
        self.produto1.config(height='200', width='200')
        self.produto1.pack(side='top')

        # FRAME 2
        self.peso1 = ttk.Frame(self.cadastro)
        # LABEL 2
        self.label2 = ttk.Label(self.peso1)
        self.label2.config(text='Peso:           ')
        self.label2.pack(side='left')
        # ENTRY 2
        self.pes1 = ttk.Entry(self.peso1)
        self.pes1.pack(side='left')
        # FINALIZANDO FRAME 2
        self.peso1.config(height='200', width='200')
        self.peso1.pack(side='top')

        # FRAME 3
        self.produto2 = ttk.Frame(self.cadastro)
        # LABEL 3
        self.label3 = ttk.Label(self.produto2)
        self.label3.config(text='Produto 2:  ')
        self.label3.pack(side='left')
        # ENTRY 3
        self.prod2 = ttk.Entry(self.produto2)
        self.prod2.pack(side='left')
        # FINALIZANDO FRAME 3
        self.produto2.config(height='200', width='200')
        self.produto2.pack(side='top')

        # FRAME 4
        self.peso2 = ttk.Frame(self.cadastro)
        # LABEL 4
        self.label4 = ttk.Label(self.peso2)
        self.label4.config(text='Peso:           ')
        self.label4.pack(side='left')
        # ENTRY 4
        self.pes2 = ttk.Entry(self.peso2)
        self.pes2.pack(side='left')
        # FINALIZANDO FRAME 4
        self.peso2.config(height='200', width='200')
        self.peso2.pack(side='top')

        # FRAME 5
        self.produto3 = ttk.Frame(self.cadastro)
        # LABEL 5
        self.label5 = ttk.Label(self.produto3)
        self.label5.config(text='Produto 3:  ')
        self.label5.pack(side='left')
        # ENTRY 5
        self.prod3 = ttk.Entry(self.produto3)
        self.prod3.pack(side='left')
        # FINALIZANDO FRAME 5
        self.produto3.config(height='200', width='200')
        self.produto3.pack(side='top')

        # FRAME 6
        self.peso3 = ttk.Frame(self.cadastro)
        # LABEL 6
        self.label6 = ttk.Label(self.peso3)
        self.label6.config(text='Peso:           ')
        self.label6.pack(side='left')
        # ENTRY 6
        self.pes3 = ttk.Entry(self.peso3)
        self.pes3.pack(side='left')
        # FINALIZANDO FRAME 6
        self.peso3.config(height='200', width='200')
        self.peso3.pack(side='top')

        # FINALIZANDO FRAME CADASTRO
        self.cadastro.config(height='200', width='200')
        self.cadastro.pack(padx='20', pady='20', side='left')

        # RESULTADO
        # FRAME RESULTADO
        self.resultado = ttk.Frame(self.menu)

        # FRAME RESULTADO 1 (PRODUTO 1/ PESO 1)
        self.res1 = ttk.Frame(self.resultado)
        # ENTRY PRODUTO 1
        self.rprod1 = ttk.Entry(self.res1)
        self.rprod1.pack(ipadx='10', padx='10', side='left')
        # ENTRY PESO 1
        self.rpes1 = ttk.Entry(self.res1)
        self.rpes1.pack(padx='10', side='top')
        # FINALIZANDO FRAME RESULTADO 1
        self.res1.config(height='200', width='200')
        self.res1.pack(pady='5', side='top')

        # FRAME RESULTADO 2 (PRODUTO 2/ PESO 2)
        self.res2 = ttk.Frame(self.resultado)
        # ENTRY PRODUTO 2
        self.rprod2 = ttk.Entry(self.res2)
        self.rprod2.pack(ipadx='10', padx='10', side='left')
        # ENTRY PESO 2
        self.rpes2 = ttk.Entry(self.res2)
        self.rpes2.pack(padx='10', side='top')
        # FINALIZANDO FRAME RESULTADO 2
        self.res2.config(height='200', width='200')
        self.res2.pack(pady='5', side='top')

        # FRAME RESULTADO 3 (PRODUTO 3/ PESO 3)
        self.res3 = ttk.Frame(self.resultado)
        # ENTRY PRODUTO 3
        self.rprod3 = ttk.Entry(self.res3)
        self.rprod3.pack(ipadx='10', padx='10', side='left')
        # ENTRY PESO 3
        self.rpes3 = ttk.Entry(self.res3)
        self.rpes3.pack(padx='10', side='top')
        # FINALIZANDO FRAME RESULTADO 3
        self.res3.config(height='200', width='200')
        self.res3.pack(pady='5', side='top')

        # FINALIZANDO FRAME RESULTADO
        self.resultado.config(height='200', width='200')
        self.resultado.pack(side='left')

        # FINALIZANDO FRAME MENU
        self.menu.config(height='200', width='200')
        self.menu.pack(side='top')

        self.mainwindow = self.menu

    def lerValores(self):
        prodlist = list()
        prodlist.append(self.prod1)
        

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Auto Fomula M1')
    app = MenuFormula(root)
    app.run()
