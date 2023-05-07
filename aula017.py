'''
lista = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
lista[3] = 'Cerveja'
lista.append('Cokkie')
lista.insert(0, 'Cachorro quente')
#del lista[3]
#lista.pop(3)
lista.remove('Pizza')
for v in lista:
    print(v, end=' ')
'''
'''Valores = list(range(4, 11))  # Declarando os valores da lista com range.
for v in Valores:
    print(v, end=' ')
'''
'''
Valores = [8, 3, 7, 9, 20]
#Valores.sort()  # Declarando que minha lista vai receber uma ordem crescente...
Valores.sort(reverse=True)  # Declarando que minha lista vai receber uma ordem decrescente...
for v in Valores:
    print(v, end=' ')
'''
'''Valores = []
Valores.append(3)
Valores.append(7)
Valores.append(9)
for p, v in enumerate(Valores):
    print(f'Na posição {p} encontrei o valor {v}...')
print('Final da minha Lista')
'''
'''
Valores = list()
for cont in range(0, 3):
    Valores.append(int(input('Digite um valor: ')))
for p, v in enumerate(Valores):
    print(f'Na posição {p} encontrei o valor {v}!')
'''

a = [4, 5, 3, 9]
#b = a  # Ligação de lista
b = a[:]  # Cópia de lista
b[2] = 22
print(f'A lista A: {a}')
print(f'A lista B: {b}')

