# Exercise 053
import os
os.system('clear')
input('Press enter to start... ')
print('=-=' * 15)
print(' Palindrome Detector ')
print('=-=' * 15)
print('''Type a phrase or word and i´ll
inform if is a palindrome or not!''')
print('-' * 1)
phrase = str(input('Type a word or phrase: ')).strip().lower()
word = phrase.split()
join = ''.join(word)
reverse = ''
for c in range(len(join) -1, -1, -1):
    reverse += join[c]
print('The typed frase: {} and your reverse is: {}!'.format(phrase, reverse))
if join == reverse:
    print('PALINDROME!')
else:
    print('Not a PALINDROME!')
