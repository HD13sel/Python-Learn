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

        # FRAME 7
        self.produto4 = ttk.Frame(self.cadastro)
        # LABEL 7
        self.label7 = ttk.Label(self.produto4)
        self.label7.config(text='Produto 4:  ')
        self.label7.pack(side='left')
        # ENTRY 7
        self.prod4 = ttk.Entry(self.produto4)
        self.prod4.pack(side='left')
        # FINALIZANDO FRAME 7
        self.produto4.config(height='200', width='200')
        self.produto4.pack(side='top')

        # FRAME 8
        self.peso4 = ttk.Frame(self.cadastro)
        # LABEL 8
        self.label8 = ttk.Label(self.peso4)
        self.label8.config(text='Peso:           ')
        self.label8.pack(side='left')
        # ENTRY 8
        self.pes4 = ttk.Entry(self.peso4)
        self.pes4.pack(side='left')
        # FINALIZANDO FRAME 8
        self.peso4.config(height='200', width='200')
        self.peso4.pack(side='top')

        # FRAME 9
        self.produto5 = ttk.Frame(self.cadastro)
        # LABEL 9
        self.label9 = ttk.Label(self.produto5)
        self.label9.config(text='Produto 5:  ')
        self.label9.pack(side='left')
        # ENTRY 9
        self.prod5 = ttk.Entry(self.produto5)
        self.prod5.pack(side='left')
        # FINALIZANDO FRAME 9
        self.produto5.config(height='200', width='200')
        self.produto5.pack(side='top')

        # FRAME 10
        self.peso5 = ttk.Frame(self.cadastro)
        # LABEL 10
        self.label10 = ttk.Label(self.peso5)
        self.label10.config(text='Peso:           ')
        self.label10.pack(side='left')
        # ENTRY 10
        self.pes5 = ttk.Entry(self.peso5)
        self.pes5.pack(side='left')
        # FINALIZANDO FRAME 10
        self.peso5.config(height='200', width='200')
        self.peso5.pack(side='top')

        # FRAME 11
        self.produto6 = ttk.Frame(self.cadastro)
        # LABEL 11
        self.label11 = ttk.Label(self.produto6)
        self.label11.config(text='Produto 6:  ')
        self.label11.pack(side='left')
        # ENTRY 11
        self.prod6 = ttk.Entry(self.produto6)
        self.prod6.pack(side='left')
        # FINALIZANDO FRAME 11
        self.produto6.config(height='200', width='200')
        self.produto6.pack(side='top')

        # FRAME12
        self.peso6 = ttk.Frame(self.cadastro)
        # LABEL 12
        self.label12 = ttk.Label(self.peso6)
        self.label12.config(text='Peso:           ')
        self.label12.pack(side='left')
        # ENTRY 12
        self.pes6 = ttk.Entry(self.peso6)
        self.pes6.pack(side='left')
        # FINALIZANDO FRAME 12
        self.peso6.config(height='200', width='200')
        self.peso6.pack(side='top')

        # FRAME 13
        self.produto7 = ttk.Frame(self.cadastro)
        # LABEL 13
        self.label13 = ttk.Label(self.produto7)
        self.label13.config(text='Produto 7:  ')
        self.label13.pack(side='left')
        # ENTRY 13
        self.prod7 = ttk.Entry(self.produto7)
        self.prod7.pack(side='left')
        # FINALIZANDO FRAME 13
        self.produto7.config(height='200', width='200')
        self.produto7.pack(side='top')

        # FRAME 14
        self.peso7 = ttk.Frame(self.cadastro)
        # LABEL 14
        self.label14 = ttk.Label(self.peso7)
        self.label14.config(text='Peso:           ')
        self.label14.pack(side='left')
        # ENTRY 14
        self.pes7 = ttk.Entry(self.peso7)
        self.pes7.pack(side='left')
        # FINALIZANDO FRAME 14
        self.peso7.config(height='200', width='200')
        self.peso7.pack(side='top')

        # FRAME 15
        self.produto8 = ttk.Frame(self.cadastro)
        # LABEL 15
        self.label15 = ttk.Label(self.produto8)
        self.label15.config(text='Produto 8:  ')
        self.label15.pack(side='left')
        # ENTRY 15
        self.prod8 = ttk.Entry(self.produto8)
        self.prod8.pack(side='left')
        # FINALIZANDO FRAME 15
        self.produto8.config(height='200', width='200')
        self.produto8.pack(side='top')

        # FRAME 16
        self.peso8 = ttk.Frame(self.cadastro)
        # LABEL 16
        self.label16 = ttk.Label(self.peso8)
        self.label16.config(text='Peso:           ')
        self.label16.pack(side='left')
        # ENTRY 16
        self.pes8 = ttk.Entry(self.peso8)
        self.pes8.pack(side='left')
        # FINALIZANDO FRAME 16
        self.peso8.config(height='200', width='200')
        self.peso8.pack(side='top')

        # FRAME 17
        self.produto9 = ttk.Frame(self.cadastro)
        # LABEL 17
        self.label17 = ttk.Label(self.produto9)
        self.label17.config(text='Produto 9:  ')
        self.label17.pack(side='left')
        # ENTRY 17
        self.prod9 = ttk.Entry(self.produto9)
        self.prod9.pack(side='left')
        # FINALIZANDO FRAME 17
        self.produto9.config(height='200', width='200')
        self.produto9.pack(side='top')

        # FRAME 18
        self.peso9 = ttk.Frame(self.cadastro)
        # LABEL 18
        self.label18 = ttk.Label(self.peso9)
        self.label18.config(text='Peso:           ')
        self.label18.pack(side='left')
        # ENTRY 18
        self.pes9 = ttk.Entry(self.peso9)
        self.pes9.pack(side='left')
        # FINALIZANDO FRAME 18
        self.peso9.config(height='200', width='200')
        self.peso9.pack(side='top')

        # FRAME 19
        self.produto10 = ttk.Frame(self.cadastro)
        # LABEL 19
        self.label19 = ttk.Label(self.produto10)
        self.label19.config(text='Produto 10:')
        self.label19.pack(side='left')
        # ENTRY 19
        self.prod10 = ttk.Entry(self.produto10)
        self.prod10.pack(side='left')
        # FINALIZANDO FRAME 19
        self.produto10.config(height='200', width='200')
        self.produto10.pack(side='top')

        # FRAME 20
        self.peso10 = ttk.Frame(self.cadastro)
        # LABEL 20
        self.label20 = ttk.Label(self.peso10)
        self.label20.config(text='Peso:           ')
        self.label20.pack(side='left')
        # ENTRY 20
        self.pes10 = ttk.Entry(self.peso10)
        self.pes10.pack(side='left')
        # FINALIZANDO FRAME 20
        self.peso10.config(height='200', width='200')
        self.peso10.pack(side='top')

        # FRAME SOMA
        self.soma = ttk.Frame(self.cadastro)
        # SEPARATOR
        self.separator_1 = ttk.Separator(self.soma)
        self.separator_1.config(orient='horizontal')
        self.separator_1.pack(fill='x', pady='20', side='top')
        # LABEL SOMA
        self.label_26 = ttk.Label(self.soma)
        self.label_26.config(text='SOMA:         ')
        self.label_26.pack(side='left')
        # ENTRY SOMA
        self.somapeso = ttk.Entry(self.soma)
        self.somapeso.pack(side='top')
        # FINALIZANDO FRAME SOMA
        self.soma.config(height='200', width='200')
        self.soma.pack(pady='10', side='top')

        # FINALIZANDO FRAME CADASTRO
        self.cadastro.config(height='200', width='200')
        self.cadastro.pack(padx='20', pady='20', side='left')

        # OC
        # FRAME OC
        self.oc = ttk.Frame(self.menu)

        # FRAME TONELADS
        self.tonel = ttk.Frame(self.oc)
        # LABEL TONELADAS
        self.toneladas = ttk.Label(self.tonel)
        self.toneladas.config(text='TONELADAS:')
        self.toneladas.pack(side='top')
        # ENTRY TONELADAS
        self.ton = ttk.Entry(self.tonel)
        self.ton.pack(pady='10', side='top')
        # FINALIZANDO FRAME TONELADAS
        self.tonel.config(height='200', width='200')
        self.tonel.pack(pady='20', side='top')

        # FRAME VOLUME
        self.volu = ttk.Frame(self.oc)
        # LABEL VOLUME
        self.volume = ttk.Label(self.volu)
        self.volume.config(text='       VOLUME: \n'
                           '(Uréia/Nitrogenado)')
        self.volume.pack(side='top')

        # RADIOBUTTON (SIM)
        self.rby = ttk.Radiobutton(self.volu)
        self.rby.config(text='SIM')
        self.rby.pack(side='left')

        # RADIOBUTTON (NAO)
        self.rbn = ttk.Radiobutton(self.volu)
        self.rbn.config(text='NÃO')
        self.rbn.pack(side='top')

        # FINALIZANDO FRAME VOLUMES
        self.volu.config(height='200', width='200')
        self.volu.pack(pady='20', side='top')

        #############################################
        # PESO EXTRA
        # FRAME PESO EXTRA
        self.extrap = ttk.Frame(self.oc)
        # LABEL PESO EXTRA
        self.pesoex = ttk.Label(self.extrap)
        self.pesoex.config(text='PESO EXTRA:')
        self.pesoex.pack(pady='0', side='top')
        # ENTRY PESO EXTRA
        self.pextra = ttk.Entry(self.extrap)
        self.pextra.pack(side='top')
        # FINALIZANDO FRAME PESO EXTRA
        self.extrap.config(height='200', width='200')
        self.extrap.pack(pady='20', side='top')

        ################################################
        # BOTAO OK
        # FRAME BOTAO
        self.botao = ttk.Frame(self.oc)
        # BUTTON
        self.botaook = ttk.Button(self.botao)
        self.botaook.config(cursor='arrow', state='normal', text='OK')
        self.botaook.pack(ipadx='20', ipady='20', side='bottom')
        # FINALIZANDO FRAME BOTAO
        self.botao.config(height='200', width='200')
        self.botao.pack(pady='20', side='top')

        # FINALIZANDO FRAME OC
        self.oc.config(height='200', width='200')
        self.oc.pack(padx='20', side='left')

        # RESULTADO
        # FRAME RESULTADO
        self.resultado = ttk.Frame(self.menu)

        # FRAME PROPRIEDADES
        self.resprop = ttk.Frame(self.resultado)

        # LABEL PRODUTO/PROPRIEDADES
        self.label_29 = ttk.Label(self.resprop)
        self.label_29.config(text='PRODUTO')
        self.label_29.pack(ipadx='55', side='left')
        self.label_30 = ttk.Label(self.resprop)

        # LABEL PESO/PROPRIEDADES
        self.label_30.config(text='PESO')
        self.label_30.pack(ipadx='35', side='left')
        # FINALIZANDO FRAME PROPRIEDADES
        self.resprop.config(height='200', width='200')
        self.resprop.pack(side='top')

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

        # FRAME RESULTADO 4 (PRODUTO 4/ PESO 4)
        self.res4 = ttk.Frame(self.resultado)
        # ENTRY PRODUTO 4
        self.rprod4 = ttk.Entry(self.res4)
        self.rprod4.pack(ipadx='10', padx='10', side='left')
        # ENTRY PESO 4
        self.rpes4 = ttk.Entry(self.res4)
        self.rpes4.pack(padx='10', side='top')
        # FINALIZANDO FRAME RESULTADO 4
        self.res4.config(height='200', width='200')
        self.res4.pack(pady='5', side='top')

        # FRAME RESULTADO 5 (PRODUTO 5/ PESO 5)
        self.res5 = ttk.Frame(self.resultado)
        # ENTRY PRODUTO 5
        self.rprod5 = ttk.Entry(self.res5)
        self.rprod5.pack(ipadx='10', padx='10', side='left')
        # ENTRY PESO 5
        self.rpes5 = ttk.Entry(self.res5)
        self.rpes5.pack(padx='10', side='top')
        # FINALIZANDO FRAME RESULTADO 5
        self.res5.config(height='200', width='200')
        self.res5.pack(pady='5', side='top')

        # FRAME RESULTADO 6 (PRODUTO 6/ PESO 6)
        self.res6 = ttk.Frame(self.resultado)
        # ENTRY PRODUTO 6
        self.rprod6 = ttk.Entry(self.res6)
        self.rprod6.pack(ipadx='10', padx='10', side='left')
        # ENTRY PESO 6
        self.rpes6 = ttk.Entry(self.res6)
        self.rpes6.pack(padx='10', side='top')
        # FINALIZANDO FRAME RESULTADO 6
        self.res6.config(height='200', width='200')
        self.res6.pack(pady='5', side='top')

        # FRAME RESULTADO 7 (PRODUTO 7/ PESO 7)
        self.res7 = ttk.Frame(self.resultado)
        # ENTRY PRODUTO 7
        self.rprod7 = ttk.Entry(self.res7)
        self.rprod7.pack(ipadx='10', padx='10', side='left')
        # ENTRY PESO 7
        self.rpes7 = ttk.Entry(self.res7)
        self.rpes7.pack(padx='10', side='top')
        # FINALIZANDO FRAME RESULTADO 7
        self.res7.config(height='200', width='200')
        self.res7.pack(pady='5', side='top')

        # FRAME RESULTADO 8 (PRODUTO 8/ PESO 8)
        self.res8 = ttk.Frame(self.resultado)
        # ENTRY PRODUTO 8
        self.rprod8 = ttk.Entry(self.res8)
        self.rprod8.pack(ipadx='10', padx='10', side='left')
        # ENTRY PESO 8
        self.rpes8 = ttk.Entry(self.res8)
        self.rpes8.pack(padx='10', side='top')
        # FINALIZANDO FRAME RESULTADO 8
        self.res8.config(height='200', width='200')
        self.res8.pack(pady='5', side='top')

        # FRAME RESULTADO 9 (PRODUTO 9/PESO 9)
        self.res9 = ttk.Frame(self.resultado)
        # ENTRY PRODUTO 9
        self.rprod9 = ttk.Entry(self.res9)
        self.rprod9.pack(ipadx='10', padx='10', side='left')
        # ENTRY PESO 9
        self.rpes9 = ttk.Entry(self.res9)
        self.rpes9.pack(padx='10', side='top')
        # FINALIZANDO FRAME RESULTADO 9
        self.res9.config(height='200', width='200')
        self.res9.pack(pady='5', side='top')

        # FRAME RESULTADO 10 (PRODUTO 10/ PESO 10)
        self.res10 = ttk.Frame(self.resultado)
        # ENTRY PRODUTO 10
        self.rprod10 = ttk.Entry(self.res10)
        self.rprod10.pack(ipadx='10', padx='10', side='left')
        # ENTRY PESO 10
        self.rpes10 = ttk.Entry(self.res10)
        self.rpes10.pack(padx='10', side='top')
        # FINALIZANDO FRAME RESULTADO 10
        self.res10.config(height='200', width='200')
        self.res10.pack(pady='5', side='top')

        # FRAME BATIDAS
        self.batidas = ttk.Frame(self.resultado)
        # LABEL BATIDAS
        self.labelbat = ttk.Label(self.batidas)
        self.labelbat.config(text='TOTAL DE BATIDAS:')
        self.labelbat.pack(ipadx='10', padx='20', side='top')
        # ENTRY BATIDAS
        self.bat = ttk.Entry(self.batidas)
        self.bat.pack(ipadx='5', ipady='5', side='top')
        # FINALIZANDO FRAME BATIDAS
        self.batidas.config(height='200', width='200')
        self.batidas.pack(side='left')

        # FRAME PESO TOTAL
        self.pesotot = ttk.Frame(self.resultado)
        # LABEL PESO TOTAL
        self.labelptot = ttk.Label(self.pesotot)
        self.labelptot.config(text='PESO TOTAL:')
        self.labelptot.pack(side='top')
        # ENTRY PESO TOTAL
        self.ptot = ttk.Entry(self.pesotot)
        self.ptot.pack(ipady='5', side='top')
        # FINALIZANDO FRAME PESO TOTAL
        self.pesotot.config(height='200', width='200')
        self.pesotot.pack(side='top')

        # FINALIZANDO FRAME RESULTADO
        self.resultado.config(height='200', width='200')
        self.resultado.pack(side='left')

        # FINALIZANDO FRAME MENU
        self.menu.config(height='200', width='200')
        self.menu.pack(side='top')

        # Main widget
        self.mainwindow = self.menu
    def lercadastro(self):
        pass

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Auto Fomula M1')
    app = MenuFormula(root)
    app.run()
