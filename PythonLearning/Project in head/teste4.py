class MeuObjeto:
    def __init__(self, n, i):
        self.nome = n
        self.idade = i
        print('Construtor chamado com sucesso')

    def imprime(self, x):
        print(f'Ola meu nome é {self.nome} e eu tenho {self.idade} anos.')
        print(x)

eumesm = MeuObjeto('Henrique', 25)

eumesm.imprime(5)
