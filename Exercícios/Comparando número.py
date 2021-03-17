# Exercício 038
print('-' * 15)
print('''Escreva dois números inteiros
e eu falarei qual o maior, qual o menor 
e se o dois são iguais.''')
print('-' * 15)
número1 = int(input('Digite o primeiro número: '))
número2 = int(input('Digite o segundo número: '))
if número1 > número2:
    print('O primeiro valor é maior!')
elif número1 < número2:
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior, os dois são iguais!')
