# Exercício 045
import os, time
from random import randint
os.system('clear')
print('#' * 50)
print('{:#^50}'.format(' GAME: pedra, papel ou tesoura '))
print('#' * 50)
print('Vamos jogar pedra, papel ou tesoura?!')
print('-' * 1)
input('Aperte enter para começar...')
print('-' * 1)
print('Suas opções: ')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
print('-' * 1)
jogador = int(input('Faça a sua jogada: '))
itens = ('Pedra', 'Papel', 'Tesoura')
bot = randint(0, 2)
print('-' * 1)
time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ!!!')
print('-=-' * 30)
print('JOGADOR jogou {}!'.format(itens[jogador]))
print('O COMPUTADOR jogou {}!'.format(itens[bot]))
print('-=-' * 30)
if bot == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('Jogada INVÁLIDA!')
elif bot == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('Jogada INVÁLIDA!')
elif bot == 2:
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('BOT VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada INVÁLIDA!')
input('Aperte enter para encerrar o jogo!')
os.system('clear')
