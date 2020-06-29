def notas(*num, sit=False):
    """
    --> Função para analisar várias notas de uma turma, com média e situação(opcional) da turma.
    :param num: Um ou mais valores de notas dos alunos da turma.
    :param sit: Valor opcional, True para mostrar situacao da turma. Padrão é falso.
    :return: Retorna em um dicionário com varias informaçôes e situação da turma.
    """
    dados = dict()
    dados['total'] = len(num)
    dados['maior'] = max(num)
    dados['menor'] = min(num)
    dados['media'] = sum(num)/len(num)
    if sit:
        if dados['media'] >= 7:
            dados['situacao'] = 'EXCELENTE'
        elif dados['media'] >= 5:
            dados['situacao'] = 'RAZOAVEL'
        else:
            dados['sitaucao'] = 'PESSIMO'
    return dados


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
