# 1° Interactive Help
# - - help(print)
# - - print(input.__doc__)

# 2° DocStrings
'''
def contador(i, f, p):
    """
     Faz uma contagem e mostra na tela.
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return:  Retorna do inicio ao fim de passo em passo
    """
    cont = i
    while cont <= f:
        print(cont, end='-')
        cont += p
    print('FIM!')


# Programa Principal
contador(0, 10, 2)
help(contador)
'''

# 3° Parametros opcionais

'''
def somar(a=0, b=0, c=0, d=0):
    s = a + b + c + d
    print(s)


somar(5, 3, 2)
somar(8, 4)
somar()
somar(1, 2, 3, 4)
'''

# 4° Escopo de Variáveis

'''
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A Dentro vale {a}')
    print(f'B Dentro vale {b}')
    print(f'C Dentro vale {c}')


a = 5
teste(a)
print(f'A Fora vale {a}')
'''

# 5° Retorno de valores
'''
def somar(a=0, b=0, c=0):
    soma = a + b + c
    return soma


resp = somar(10, 10, 10)
resp1 = somar(10, 10)
resp2 = somar(10, 5)
print(f'a soma dos valores é {resp} | {resp1} | {resp2}')
'''
'''
def fatorial(num=1):
    f = 1
    for c in range(num, 0, - 1):
        f *= c
    return f


print(fatorial(5))
'''
def parOUimpar(num):
    if num % 2 == 0:
        return True
    else:
        return False


n = int(input('Digite um número: '))
print(parOUimpar(n))
if parOUimpar(n):
    print('é par')
else:
    print('é impar')

