# Estrutura de repetição For
'''
for c in range(0, 6):
    print('Oi')
print('Fim')
'''

# Como fazer uma contagem regressiva
'''for c in range(6, 0, -1): # Passo - 1 ou seja de 6 ate 0 vai tirando 1 = 6, 5, 4, 3, 2, 1.
    print(c)
print('FIM')'''

# Considerando o conceito do passo, você pode testar varios parametros...
'''for c in range(0, 110, 10):
    print(c)
print('FIM')'''
'''for c in range(0, 7, 2):
    print(c)
print('FIM')'''
'''for c in range(50, - 10, - 10):
    print(c)
print('FIM')'''

# Vejamos um exemplo a seguir, interagindo com o úsuario...
'''n = int(input('Digite um número: '))
for c in range(0, n+1): # ao adicionar o + 1, o computador considera o último número
    print(c)'''

# Agora o  úsuario decide o começo o fim e o passo a ser feito na minha estrutura (for)...
'''inicio  = int(input('Inicio da contagem: '))
fim = int(input('Fim da contagem: '))
passo = int(input('de qts em qts: '))
for c in range(inicio, fim + 1, passo):
    print(c)'''

# Tambem da para pedir para o usuario digitar quantas vezes quiser dentro de um (for)...
'''for c in range(0, 3):
    n = int(input('Digite um numero: '))'''

# Fazendo uma soma com estrutura (for)...
s = 0
for c in range(0, 5):
    n = int(input('N: '))
    s += n # Lembrando que += , é  S recebe S mais N
print(s)