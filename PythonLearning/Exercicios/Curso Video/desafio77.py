palavras = ('Fertilizantes', 'Bag', 'Tonelada', 'Sacaria', 'Misturador', 'Caminhao', 'Carregamento', 'Domino',
            'Moega', 'Pa Carregadeira', 'Empilhadeira', 'Cafe', 'Ordem de Carga', 'Heringer', 'kcl')

for p in palavras:
    print(f'\nA palavra {p.upper()} tem essas vogais: ', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(f'{letras}', end=' ')

