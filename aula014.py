'''for c in range(1, 10):
    print(c)
print('Fim')

c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')

for c in range(1, 5):
    num = int(input('Digite um número: '))
print('Fim')

c = 1
while c != 0:
    c = int(input('Digite um valor: '))
print('fim')

r = 'S'
while r == 'S':
    num = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S/N]? ')).upper()
print('Fim')
'''
c = 1
par = impar = 0
while c != 0:
    c = int(input('Digite um valor: '))
    if c != 0:
        if c % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} pares, e {} impares.'.format(par, impar))


