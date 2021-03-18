# Exercício 043
import os, time
os.system('clear')
print('#' * 36)
print('##### Índice de massa corporal #####')
print('#' * 36)
print('-' * 15)
print('''Indique a sua altura e peso
e eu informarei se você está: abaixo do peso,
no peso ideal, sobrepeso, obesidade ou
obesidade mórbida, tudo isso com base no IMC.''')
print('-' * 1)
time.sleep(1)
input('Pressione enter para continuar!')
print('-' * 5)
peso = float(input('Informe o seu peso(em quilos): '))
altura = float(input('Informe a sua altura(em metros): '))
imc = peso / altura ** 2
print('Analisando peso...')
time.sleep(1)
print('O seu índice de massa corporal é {:.1f}!'.format(imc))
print('-' * 1)
if imc < 18.5:
    print('O seu status atual é: ABAIXO DO PESO!')
elif imc < 25:
    print('O seu status atual é: PESO IDEAL!')
elif imc < 30:
    print('O seu status atual é: SOBREPESO!')
elif imc < 40:
    print('O seu status atual é: OBESIDADE!')
else:
    print('OBESIDADE MÓRBIDA!')
print('-' * 4)
input('Pressione enter para encerrar! ')
os.system('clear')
