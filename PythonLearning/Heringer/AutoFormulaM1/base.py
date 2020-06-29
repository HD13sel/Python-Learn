'''
Básico
Baseado em um lugar onde trabalho onde utilizamos OC (Ordem de cargas) contendo no máximo 15 produtos (mpx), cada um com peso
específico (px) e todos os produtos com seus pesos vão somar para dar 1000. Na OC também contém as toneladas (ton) que vai ser a quantidade total do
pedido. Lembrando que temos que converter essas quantidades para um peso de batida (bat), ou seja, um peso que a betoneira do máquinario suporta, se 
for muito volumosa o total é 8000, senão é 12000. Ai convertemos todos os pesos dos produtos para que o total atinga a batelada. E também acrescentamos
um peso extra (pext) para em casos de derrames imprevistos durante o trajeto do máquinario.
Porém, um exemplo se temos um carga de 32 tons sem produto volumoso, não iria caber 32000 em 12000, porem temos que especificar quantas bateladas (btl)
vão ser de cada batida (bat)

# O sistema vai receber no máximo 15 produtos (mp) e os pesos respectivos (p), após isso o usuario deverá informar quantas toneladas (ton) são, informar
qual vai ser o tipo de produto se é volumoso ou não (ure) e também vai informar qual vai ser o peso extra (pext)
'''
ton = int(input('Quantas toneladas tem a OC: '))
ure = str(input('A formula é muito volumosa: [s/n] '))
pext = int(input('Deseja colocar mais quantos kg: '))

# Vai diferenciar se o produto contém muito volume ou não!

if ure in 'S''s''Sim''sim':    
    for btl in range(1,51):
        bat = (ton + pext)/btl  # Vai pegar as ton e somar com pext e fazer a conversão de quantas batidas vão ser
        if bat < 8000:
            print(f'Vai ser {btl} batidas com o total de {bat:.2f}')
            break                
else:
    for btl in range(1,51):
        bat = (ton + pext)/btl
        if bat < 12000:
            print(f'Vai ser {btl} batidas com total de {bat:.2f}')
            break 
