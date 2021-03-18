# Exercício 040
import os, time
os.system('clear')
print('=-=' * 30)
print('     AQUELE CLÁSSICO DA MÉDIA     ')
print('=-=' * 30)
print('-' * 15)
print('''Média abaixo de 5.0: REPROVADO!
Média entre 5.0 e 6.9: RECUPERAÇÃO!
Média 7.0 ou superior: APROVADO!''')
print('-' * 15)
nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
média = (nota1 + nota2) / 2
print('A sua média é de {:.1f}!'.format(média))
if média >= 7:
    print('O aluno está APROVADO!')
elif média > 5 and média < 6.9:
    print('O aluno está em RECUPERAÇÃO!')
elif média < 4.9:
    print('O aluno está REPROVADO!')
time.sleep(1)
input('Aperte enter para encerrar...')
os.system('clear')
