# Exercise 047
import os
os.system('clear')
print('-=' * 25)
print(' Even Numbers Count ')
print('-=' * 25)
print('''I'll show you only the even numbers
between 0 and 50!''')
print('-' * 1)
input('Press enter to start... ')
amount = 0
for c in range(0, 51, 2):
    amount += 1
    print(c, end=' ')
print('\nThe amount of even numbers between 0 and 50 are {}!'.format(amount))
input('Press enter to end... ')
os.system('clear')
