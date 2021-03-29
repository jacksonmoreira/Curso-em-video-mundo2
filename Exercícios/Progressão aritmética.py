# Exercício 051
import os
os.system('clear')
print('{:#^30}'.format(' Arithmetic Ratio '))
first = int(input('Arithmetic ratio first term: '))
ratio = int(input('Ratio of the Arithmetic ratio: '))
input('Press enter to start... ')
for c in range(1, 11):
    print(first, end=' -> ')
    first += ratio
input('\nPress enter to end... ')
os.system('clear')
