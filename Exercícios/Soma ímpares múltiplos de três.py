# Exercício 48
import os, time
os.system('clear')
print('-=' * 30)
print(' Sum odd multiples of three ')
print('-=' * 30)
print('''I'll inform you the all multiples
of 3 sum between 1 and 500!''')
print('-' * 1)
input('Press enter to start... ')
amount = 0
total = 0
for c in range(3, 501, 6):
    total += 1
    amount += c
    print(c)
'''print('The {} requested values sum are {}!'.format(total, amount))
input('Press enter to end... ')
os.system('clear')'''
