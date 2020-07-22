import tkinter
import random

# tkinter.tk é a classe base para a janela padrão. A nossa classe MegaSenaApp irá herdar todas as funcionalidades
# da classe padrão.
class MegaSenaApp(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        # No construtor da nossa classe, apenas chamamos o construtor da classe pai, tkinter.Tk.__init__().
        self.parent = parent
        # Geralmente necessitaremos de acessar o pai de um objeto. É uma boa técnica sempre salvar uma referência ao pai
        self.initialize()
        # no método initialize criamos os demais objetos que serão apresentados na tela, iniciaremos var globais.


    def initialize(self):  # no momento não inicializamos nada.
        self.grid()  # Vamos dispor os objetos na tela dentro de uma grade
        self.lblPalpite1 = tkinter.Label(self, text='01')  # Apresentará o primeiro numero
        self.lblPalpite1.grid(column=0, row=0)   # Definindo a posição
        self.lblPalpite2 = tkinter.Label(self, text='02')  # Apresentará o segundo numero
        self.lblPalpite2.grid(column=1, row=0)  # Definindo a posição
        self.lblPalpite3 = tkinter.Label(self, text='03')  # terceiro numero
        self.lblPalpite3.grid(column=2, row=0)  # posicao
        self.lblPalpite4 = tkinter.Label(self, text='04')  # quarto numero
        self.lblPalpite4.grid(column=4, row=0)  # posicao
        self.lblPalpite5 = tkinter.Label(self, text='05')  # quinto numero
        self.lblPalpite5.grid(column=5, row=0)  # posicao
        self.lblPalpite6 = tkinter.Label(self, text='06')  # sexto numero
        self.lblPalpite6.grid(column=6, row=0)  # posicao

        self.btnGeraPalpite = tkinter.Button(self, text=u'Estou com sorte!',  # Criamos um botão
                                             command=self.OnButtonGeraPalpiteClick)  # Associamos o método clicar botão
        self.btnGeraPalpite.grid(column=3, row=1)  # colocamos na posicao, coluna 3 e linha 1.

    def OnButtonGeraPalpiteClick(self):  # Cria um valor aleatório entre 1 e 60 e apresenta na label.
        val = random.randint(1, 61)
        self.lblPalpite1.config(text=str(val))

        val = random.randint(1, 61)
        self.lblPalpite2.config(text=str(val))

        val = random.randint(1, 61)
        self.lblPalpite3.config(text=str(val))

        val = random.randint(1, 61)
        self.lblPalpite4.config(text=str(val))

        val = random.randint(1, 61)
        self.lblPalpite5.config(text=str(val))

        val = random.randint(1, 61)
        self.lblPalpite6.config(text=str(val))


# Este é o ponto onde o programa se inicia.
# Se foi chamado a partir do interpretador python, o __name__ automaticamente será '__main__'

if __name__ == '__main__':
    app = MegaSenaApp(None)  # Criamos uma aplicação sem nenhum pai, pois é a principal.
    app.title('Mega Senando')
    app.mainloop()
