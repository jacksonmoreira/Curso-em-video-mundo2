# Exercicio 050
import os, time
os.system('clear')
soma = 0
cont = 0
input('Aperte enter para iniciar... ')
for c in range(1, 7):
    print('-' * 1)
    num = int(input('Digite o {}° valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('-' * 1)
time.sleep(1)
print('PROCESSANDO...')
print('-' * 1)
time.sleep(0.5)
print('Você informou {} números pares e a soma entre eles é {}!'.format(cont, soma))
input('Aperte enter para encerrar... ')
os.system('clear')
