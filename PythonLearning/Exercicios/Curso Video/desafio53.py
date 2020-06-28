frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f"Você digitou {frase} e o inverso dela é {inverso}")
if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('Não é um Palindromo')
