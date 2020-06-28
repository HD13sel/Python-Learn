n = s = c = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'A soma dos {c} valores é {s}!')