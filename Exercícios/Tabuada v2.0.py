# Exercício 049
print('{:#^30}'.format(' Multiplication Table v2.0 '))
print('''Insert a number
to the multiplication table!''')
num = int(input('Insert a integer: '))
for c in range(1, 9):
    print('{} x {} = {}'.format(num, c, num*c))
