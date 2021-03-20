# Exercício 051
import os, time
os.system('clear')
print('#' * 30)
print(' Progressão aritmética ')
print('#' * 30)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
conta = termo + (11 - 1) * razão
input('Pressione enter para iniciar... ')
print('-' * 1)
for c in range(termo, conta, razão):
    print('{}'.format(c), end=' -> ')
print('Acabou!')
print('-' * 1)
input('Pressione enter para encerrar... ')
os.system('clear')
