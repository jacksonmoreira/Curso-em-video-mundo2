# Exercício 041
print('-' * 15)
print('''Digite o seu ano de nascimento
e eu informarei em qual categoria de atleta
baseada na idade você se encaixa.''')
print('-' * 15)
ano = int(input('Digite o seu ano de nascimento: '))
idade = 2021 - ano
print('O atleta tem {} anos!'.format(idade))
if idade <= 9:
    print('Atleta MIRIM!')
elif idade <= 14 and idade > 9:
    print('Atleta INFANTIL!')
elif idade <= 19 and idade > 14:
    print('Atleta JÚNIOR!')
elif idade <= 25 and idade > 19:
    print('Atleta SÊNIOR!')
else:
    print('Atleta MASTER!')
