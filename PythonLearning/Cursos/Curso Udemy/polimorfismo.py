class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar o método.')

    def comer(self):
        print(f'{self.nome} está comendo..')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.nome} fala AU AU')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.nome} fala MIAU')


felix = Gato('Felix')
felix.comer()
felix.falar()

hesh = Cachorro('Hesh')
hesh.comer()
hesh.falar()

