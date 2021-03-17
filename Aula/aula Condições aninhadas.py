# Parte prática da aula 12
nome = str(input('Digite o seu nome: ').strip())
if nome == 'Jackson' or 'Cirleide':
    print('Que nome lindo você tem {}!'.format(nome))
elif nome == 'Gustavo' or 'Sandra':
    print('Que nome bonito você tem {}!'.format(nome))
elif nome in 'Felipe Márcia Danielle Verônica Edvaldo':
    print('Que nome legal você tem {}!'.format(nome))
else:
    print('Que nome feio você tem {}!'.format(nome))
print('Tenha um bom dia {}, independente de seu nome ser bonito ou não.'.format(nome))
print('--FIM DO PROGRAMA--')
