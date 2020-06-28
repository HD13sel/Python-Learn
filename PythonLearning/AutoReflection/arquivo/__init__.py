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