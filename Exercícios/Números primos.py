# Exercício 052
import os
os.system('clear')
print('=-=' * 30)
print(' Prime Numbers ')
print('=-=' * 30)
print('''Type a integer and i´ll inform
if the typed number are prime or not!''')
print('-' * 4)
number = int(input('Type a integer: '))
total = 0
for c in range(1, number+1):
    if number % c == 0:
        print('\033[1;32m', end='')
        total += 1
    else:
        print('\033[1;31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[1;34mThe number {} has been divided {} times!'.format(number, total))
if total == 2:
    print('\033[1;32mHe´s a PRIME number!\033[m')
else:
    print('\033[1;31mNot a PRIME number!\033[m')
print('-' * 1)
input('\033[1;33mPress enter to end... ')
os.system('clear')
