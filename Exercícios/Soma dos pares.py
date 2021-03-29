# Exercicio 050
print('{:#^30}'.format(' Even Numbers Sum '))
a = 0
s = 0
for c in range(1, 7):
    num = int(input('Insert a integer: '))
    if num % 2 == 0:
        a += 1
        s += num
print('The {} values sum is {}!'.format(a, s))

