'''Estruturas Condicionais'''
'''nome = input('Digite seu nome: ').upper().strip()
if nome == 'FELIPE':
    print('Que nome Lindo!')
else:
    print('Que nome Normal!')
print('Bom dia!, {}'.format(nome.title()))'''

#Estrutura simplificada
ano = int(input('Digite o ano do seu veiculo: '))
print('Veiculo novo!' if ano <= 3 else 'Veiculo velho!')