"""

Documentando funções com Docstrings

# OBS: Pdemos ter acesso a doc de uma função em Python utilizando a propriedade (__doc__), e utilizando a função help()

"""

# Exemplos
# Melhor usar no console


def diz_oi():
    """Uma função simples que retorna string 'Oi'"""
    return 'Oi! '


print(diz_oi())

print(help(diz_oi()))

print(diz_oi().__doc__)

def exponencial(numero, potencia=2):
    """
    Funções que retorna por padrão o quadrado de 'numero'.
    :param numero: Número que desejamos gerar o exponencial.
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'
    """
    return numero ** potencia
