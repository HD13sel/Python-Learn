import tkinter
import random


class MinhaApp(tkinter.Tk):
# tkinter.tk é a classe base para a janela padrão. A nossa classe MinhaApp irá herdar todas as funcionaliades da classe
# padrão
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)  # No construtor da nossa classem, apenas chamamos o construtor da classe pai,
        # tkinter.Tk.__init__()
        self.parent = parent  # Geralmente necessitaremos de acessar o pai de um objeto. É um boa tecnica sempre salvar
        # uma referencia ao pai.
        self.initialize()  # no método initialize criamos os demais objetos que serão apresentados na tela,
        # inicializamos as variaveis globais, incializamos o hardware, caso necessário, etc...

    def initialize(self):  # Aqui criamos os widgets que serão apresentados na tela.
        self.grid()  # Dispõe os objetos na tela dentro de uma grade.
        self.lblC = tkinter.Label(self, text='Graus celsius')  # Este objeto irá representar o texto de graus celsius.
        self.lblC.grid(column=0, row=0)  # Nesta posição (coluna 0 e linha 0)

        self.lblSep = tkinter.Label(self, text='<-->')  # Este objeto irá representar um tipo de separador.
        self.lblSep.grid(column=1, row=0)  # Nesta posição (coluna 1 e linha 0)

        self.lblF = tkinter.Label(self, text='Graus Fahrenheit')  # Este objeto irá representar o texto de Graus Fº
        self.lblF.grid(column=2, row=0)  # Nesta posição (coluna 2 e linha 0)

        self.entryC = tkinter.Entry(self)  # Criamos um campo de texto onde está disponivel o valor de graus Cº
        self.entryC.grid(column=0, row=1, sticky='EW')  # Deixamos na posição coluna 0 e linha 1

        self.entryF = tkinter.Entry(self)  # Criamos um campo de texto onde está disponivel o valor de graus Fº
        self.entryF.grid(column=2, row=1, sticky='EW')  # Deixamos na posição coluna 2 e linha 1

        self.btnCalculaF = tkinter.Button(self, text=u'Celsius -> Fahrenheint', command=self.OnButtonCalculaFClick)
        # Criamos o objeto botão e associamos o evento clicar botão no método OnButtonCalculaFClick.
        self.btnCalculaF.grid(column=0, row=3)  # Colocamos na posição coluna 0 e na linha 3.

        self.btnCalculaC = tkinter.Button(self, text=u'Fahrenheint -> Celsius', command=self.OnButtonCalculaCClick)
        # Criamos o objeto botão e associamos o evento clicar o botão no método OnButtonCalculaCClick.
        self.btnCalculaC.grid(column=2, row=3)  # Colocamos na posição coluna 2 e na linha 3.

    def OnButtonCalculaFClick(self):  # Calcula o valor em fahrenheint e mostra no campo correto.
        fcent = float(self.entryC.get())  # Lê o valor no campo de entrada de celsius
        ffar = (9.0 * fcent)/5 + 32.0   # calcula o valor para fazer a conversão

        self.entryF.delete(0, tkinter.END)  # Apaga o campo destino
        self.entryF.insert(0, str(ffar))  # Atualiza o campo destino com o novo valor (convertido em str())

    def OnButtonCalculaCClick(self):  # Calcula o valor em celsius e mostra no campo correto.
        ffar = float(self.entryF.get())  # Lê o valor no campo de entrade de fahrenheint
        fcent = (ffar - 32.0) * 5.0/ 9.0  # Calcula o valor para fazer a conversão

        self.entryC.delete(0, tkinter.END)  # Apaga o campo destino
        self.entryC.insert(0, str(fcent))  # Atualiza o campo destino com o novo valor (convertido em str())


# Este é o ponto onde o programa se inicia...
# Se o programa foi chamado a partir do interpretador python, o __name__ automaticamente será '__main__'[
if __name__ == '__main__':
    app = MinhaApp(None)  # Criamos uma aplicação sem nenhum pai, pois é a principal.
    app.title('Conversor C<->F')  # Especificamos o título de nossa aplicação.
    app.mainloop()  # A aplicação entra no loop de espera de eventos.

