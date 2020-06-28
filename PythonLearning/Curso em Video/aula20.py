def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(8, 7)
soma(2, 1)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
