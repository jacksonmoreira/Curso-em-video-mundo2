# Exercíco 042
import os, time
os.system('clear')
print('=-=' * 30)
print('     ANALISANDO TRIÂNGULOS v2.0     ')
print('=-=' * 30)
print('''Digite o tamanho de três segmentos de reta
e eu informarei se é possível formar um triângulo e
também se ele é escaleno, isósceles e equilátero.''')
print('-' * 15)
seg1 = float(input('Digite o tamanho do segmento: '))
seg2 = float(input('Digite o tamanho do segmento: '))
seg3 = float(input('Digite o tamanho do segmento: '))
print('-'  * 1)
print('Analisando triângulo...')
print('-' * 1)
time.sleep(1)
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('É possível formar um triângulo ', end='')
    if seg1 == seg2 == seg3:
        print('EQUILÁTERO!')
    elif seg1 != seg2 != seg3 != seg1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Não é possível formar um triângulo!')
print('-' * 1)
time.sleep(1)
input('Aperte enter para encerrar!')
os.system('clear')
