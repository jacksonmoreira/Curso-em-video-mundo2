# Parte prática da aula 13
import os, time
os.system('clear')
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
time.sleep(1)
print('A soma de todos os valores foi {}!'.format(s))
input('Aperte enter para encerrar!')
os.system('clear')
