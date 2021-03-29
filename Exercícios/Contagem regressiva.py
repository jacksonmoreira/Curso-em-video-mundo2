# Exercise 46
import os, time
os.system('clear')
print('=-' * 30)
print(' Countdown ')
print('=-' * 30)
print('''A 10 seconds countdown
to the new year begin!''')
print('-' * 1)
input('Press enter to start... ')
for c in range(10, -1, -1):
    time.sleep(1)
    print(c)
print('''BOOM, BOOM. POW!
HAPPY NEW YEAR!''')
print('-' * 1)
input('Press enter to end... ')
os.system('clear')
