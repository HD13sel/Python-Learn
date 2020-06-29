def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    if idade < 16:
        return f'Você tem {idade} anos. Não vota!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Você tem {idade} anos. Voto é opcional!'
    else:
        return f'Você tem {idade} anos. Voto é obrigatório!'


anonasc = int(input('Em que ano você nasceu? '))
print(voto(anonasc))
