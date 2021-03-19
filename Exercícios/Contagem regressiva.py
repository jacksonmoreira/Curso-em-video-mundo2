# Exercício 046
import os, time
os.system('clear')
print('#' * 31)
print('##### Contagem Regressiva #####')
print('#' * 31)
input('Pressione enter para iniciar...')
for c in range(10, -1, -1):
    time.sleep(1)
    print(c)
    sleep(0.5)
print('BUM, BUM POW!!!')
input('Pressione enter para encerrar...')
os.system('clear')
