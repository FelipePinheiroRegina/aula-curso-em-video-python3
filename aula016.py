# Criando Tuplas
'''lanche = ('hamb', 'suco', 'pizza', 'pudim')
print(lanche[-4])

for c in lanche:
    print(c)'''

#Lanche = ('Hámburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#for comida in Lanche:
 #  print(f'Eu comi um {comida}')

#for cont in range(0, len(Lanche)):
 #  print(f'Eu vou comer {Lanche[cont]} na posição {cont}')

#for pos, comida in enumerate(Lanche): # enumerate serve para númerar a posição de uma tupla ou afins. desse jeito mostrado na sintaxe.
 #   print(f'Eu vou comer {comida} na posição {pos}')
#print('Comi pra caramba!')

#print(sorted(Lanche)) #Ordem alfabetica
#print(Lanche)

a = (5, 2, 3)
b = (4, 5, 6)
c = a + b
# Concatenação de Tuplas
del(c) # Apaga a Tupla
print(c)
print(c.count(2)) # Quantas vezes o número 2 aparece nas minhas tuplas a e b.
print(c.index(6)) # Em que posição está o número 6
print(c.index(5, 1)) #Pega o valor a partir da posição 1, ou seja ele pula a posição 0 1 e começa a partir do 2.
