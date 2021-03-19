# Exercício 044
import os, time
os.system('clear')
print('#' * 37)
print('{:#^37}'.format(' Gerenciador de pagamentos '))
print('#' * 37)
print('À vista dinheiro/cheque: 10% de desconto.')
print('À vista cartão: 5% de desconto.')
print('Em até 2x no cartão: preço normal.')
print('3x ou mais no cartão: 20% de juros.')
print('-' * 4)
valor = float(input('Valor a ser pago: R$'))
cartaovista = valor - (valor * 5 / 100)
dinheirovista = valor - (valor * 10 / 100)
tresvezcartao = valor + (valor * 20 / 100)
parduasvez = valor / 2
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
print('-' * 1)
p0 = int(input('Sua opção: '))
print('-' * 1)
if p0 == 1:
    print('Você escolheu pagar à vista em dinheiro ou cheque e terá 10% de desconto!')
    print('O valor da compra será de R${:.2f}!'.format(dinheirovista))
elif p0 == 2:
    print('Você escolheu para à vista no cartão e terá 5% de desconto!')
    print('O valor da compra será de R${:.2f}!'.format(cartaovista))
elif p0 == 3:
    print('Você escolheu pagar em 2x no cartão!')
    print('O valor das parcelas será de R${:.2f}!'.format(parduasvez))
elif p0 == 4:
    parcela = int(input('Quantidade de  parcelas: '))
    print('Processando...')
    time.sleep(2)
    partresvezes = valor / parcela
    partresvezes1 = tresvezcartao + partresvezes
    p6 = tresvezcartao / parcela
    print('Sua compra será parcelada em {}x de R${:.2f}!!'.format(parcela, p6))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, tresvezcartao))
else:
    print('Opção inválida!')
time.sleep(1)
print('-' * 1)
input('Aperte enter para encerrar!')
os.system('clear')
