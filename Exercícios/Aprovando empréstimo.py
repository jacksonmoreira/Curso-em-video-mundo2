# Exercício 036
valor = float(input('Digite o valor da casa: R$'))
salário = float(input('Digite o valor do seu salário: R$'))
anos = int(input('Digite em quantos anos você pagará a casa: '))
prestação = valor / (anos * 12)
mínimo = salário * 30 / 100
if prestação <= mínimo:
    print('Para pagar uma casa de R${:.2f} em {} anos, a prestação mensal será de R${:.2f}!'.format(valor, anos, prestação))
    print('EMPRÉSTIMO NEGADO!')
else:
    print('Para pagar uma casa de R${:.2f} em {} anos, a prestação mensal será de R${:.2f}!'.format(valor, anos, prestação))
    print('EMPRÉSTIMO CONCEDIDO!')
