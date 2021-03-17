# Exercício 039
print('-' * 15)
print('''Digite o ano do seu nascimento
e eu informarei se está na hora,
se já passou da hora ou ainda não está na hora de se alistar.''')
print('-' * 15)
ano = int(input('Ano de nascimento: '))
idade = 2021 - ano
alistamento = ano + 18
alistamento1 = 18 - idade
alistamento2 = idade - 18
if idade == 18:
    print('Quem nasceu em {} tem {} anos!'.format(ano, idade))
    print('Está na hora de se alistar!')
elif idade > 18:
    print('Quem nasceu em {} tem {} anos!'.format(ano, idade))
    print('Você já deveria ter alistado-se há {} anos!'.format(alistamento2))
    print('Seu alistamento foi em {}!'.format(alistamento))
elif idade < 18:
    print('Quem nasceu em {} tem {} anos!'.format(ano, idade))
    print('Ainda faltam {} anos para você se alistar!'.format(alistamento1))
