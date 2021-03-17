# Exercício 037
print('-' * 15)
print('''Digite um número inteiro qualquer e
logo em seguida  digite: 1 para transformar em bínario,
2 para transformar em octal e 3 para trans-
formar em hexadecimal.''')
print('-' * 15)
número = int(input('Digite um número inteiro: '))
print('Escolha uma das bases pra conversão:')
print('[ 1 ] converter para binário')
print('[ 2 ] converter para octal')
print('[ 3 ] converter para hexadecimal')
conversão = int(input('Digite a sua opção: '))
binário = bin(número)
octal = oct(número)
hexadecimal = hex(número)
print('O número digitado foi {}!'.format(número))
if conversão == 1:
    print('O número digitado transformado em binário ficará:')
    print('{}.'.format(binário)[2:])
elif conversão == 2:
    print('O número digitado transformado em binário octal ficará:')
    print('{}.'.format(octal)[2:])
elif conversão == 3:
    print('O número digitado transformado em hexadecimal ficará:')
    print('{}.'.format(hexadecimal)[2:])
else:
    print('Opção inexistente!')
