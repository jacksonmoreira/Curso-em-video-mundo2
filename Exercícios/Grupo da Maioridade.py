# Exercise 054
import os, time
os.system('clear')
from datetime import date
print('{:#^30}'.format(' Maiority Group '))
input('Press enter to start... ')
count = date.today().year
biggeramount = 0
smalleramount = 0
for person in range(1,8):
    print('-' * 1)
    time.sleep(0.4)
    year = int(input('{}° person birth year: '.format(person)))
    age = count - year
    if age >= 18:   
        biggeramount += 1
    else:
        smalleramount += 1
print('-' * 1)
print('{} adults and {} minors!'.format(biggeramount, smalleramount))
print('-' * 1)
input('Press enter to end... ')
os.system('clear')
