# Exercício 049
import os, time
os.system('clear')
print('#' * 30)
print(' Tabuada v2.0 ')
print('#' * 30)
num = int(input('Digite um número para ver sua tabuada: '))
print('-' * 1)
input('Aperte enter para iniciar... ')
for c in range(1, 11):
    time.sleep(0.5)
    print('{} x {} = {}'.format(num, c, num*c))
print('-' * 1)
input('Aperte enter para encerrar... ')
os.system('clear')
