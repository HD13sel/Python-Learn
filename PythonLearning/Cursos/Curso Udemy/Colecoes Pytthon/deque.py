"""
Módulos Collections - Deque

Podemos dizer que o deque é uma lsita de alta performance.


"""

# Import

from collections import deque

# Criando deques

deq = deque('HDR')
print(deq)

# Adicionando elementos no deque

deq.append('X')  # Adiciona no final
print(deq)

deq.appendleft('Z')  # Adiciona no começo
print(deq)

# Remover elementos

print(deq.pop())  # Remove e retorna o último elemento
print(deq)

print(deq.popleft())  # Remove e retorna o primeiro elemento
print(deq)
