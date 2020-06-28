from menu import *
from arquivo import *
from time import sleep

arq = 'pessoas.txt'
if not arquivoexiste(arq):
    criararquivo(arq)
while True:
    u = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Remover cadastro', 'Sair do sistema'])
    if u == 1:  # Opção de listar o arquivo
        lerarquivo(arq)
    elif u == 2:
        titulo('NOVO CADASTRO')
        nome = str(input('\033[36mNome:\033[m ')).capitalize()
        idade = leiaint('\033[36mIdade:\033[m ')
        cadastrar(arq, nome, idade)
    elif u == 3:
        titulo('EXCLUIR CADASTRO')
        nomecadastro('Nome: ', arq)
    elif u == 4:
        titulo('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(3)
