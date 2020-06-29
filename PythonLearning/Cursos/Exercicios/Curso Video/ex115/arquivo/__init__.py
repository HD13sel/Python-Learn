from time import sleep
from menu import *
def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        print('\033[35mBuscando arquivos...\033[m')
        sleep(3)
        print('\033[35mArquivo carregado com suceeso!\033[m')
        sleep(1)
        print('\033[35mCarregando MENU...\033[m')
        sleep(3)
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        sleep(1)
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')  # wt+ - Write Text Create
        a.close()
    except:
        print('\033[31mHouve um ERRO na criação do arquivo!\033[m'.center(50))
    else:
        print('\033[35mBuscando arquivos...\033[m')
        sleep(3)
        print('\033[35mArquivo não existe. Criando arquivo...\033[m')
        sleep(2)
        print('\033[35mArquivo criado com sucesso!\033[m')
        sleep(1)
        print('\033[35mCarregando MENU...\033[m')
        sleep(3)
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        sleep(1)

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo!\033[m')
    else:
        titulo('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mHouve um ERRO na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHouve um ERRO na hora de escrever os dados!\033[m')
        else:
            print(f'Novo registro de {nome} adicionado!')
            sleep(1)
            a.close()

def nomecadastro(texto, arq):
    n = str(input(texto)).capitalize()
    with open(arq, "r+") as f:
        valor = None
        new_f = f.readlines()
        f.seek(0)  # Define a posição do ponteiro no arquivo. Nesse caso é 0
        for linha in new_f:
            dado = linha.split(';')
            if n == dado[0]:
                valor = True
                print(f'\033[32m{n} foi encontrado\033[m')
                break
            else:
                valor = False
                continue
        if valor is True:
            for line in new_f:
                if n not in line:
                    f.write(line)
            print(f'\033[31m{n} foi removido.\033[m')
            f.truncate()
        else:
            print(f'\033[31m{n} não foi encontrado\033[m')


#def remover(arq, nome, idade)
            # try:
            #     dado[0].replace(f'{dado[0]}', '')
            #     dado[1].replace(f'{dado[1]}', '')
            # except:
            #     print('\033[31mFalha na exclusão do cadastro!')