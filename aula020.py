'''def mostralinha():
    print('-' * 30)

# Programa Principal
nomecompleto = {'nome' : str(input('Primeiro nome: ')),
                'sobrenome' : str(input('Sobrenome: ')),
                'ultimonome' : str(input('Ultimo nome: '))}

mostralinha()
print(f"{nomecompleto['nome']}")
mostralinha()
print(f"{nomecompleto['sobrenome']}")
mostralinha()
print(f"{nomecompleto['ultimonome']}")
mostralinha()
'''


'''def titulo(msg):
    print('-' * 20)
    print(msg)
    print('-' * 20)


# Programa Principal
nome = str(input('Nome: '))
titulo(f'  Olá {nome}')'''


'''
def soma(x, y):
    print('=-' * 10)
    print(f'{x} + {y} = {x + y}')
    print('=-' * 10)


# Programa Principal
a = int(input('Entre com um número: '))
b = int(input('Entre com outro número: '))
soma(a, b)
'''


'''
def contador(* num):
    for v in num:
        print(f'{v} ', end='')
    print(' Fim!')


contador(2, 10)
contador(1, 2, 3, 4, 5, 6)
contador(6, 8, 4)
'''


'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


lista = [5, 10, 15]
print(lista)
dobra(lista)
print(lista)
'''


def soma(* valores):
    s = 0
    for v in valores:
        s += v
    print(f'A soma dos valores {valores} é igual a {s}')


soma(5, 2)
soma(10, 3, 4, 9)


