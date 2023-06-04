'''pessoas = [('Felipe', 24), ('Daniel', 23), ('Camille', 22), ('Larissa', 24)]
print(pessoas[0])
print(pessoas[3][1])
print(pessoas[2][0])
'''
'''pessoa = list()
pessoa.append('Felipe')
pessoa.append(24)
galera = list()
galera.append(pessoa[:])
pessoa[0] = ('Larrisa')
pessoa[1] = (23)
galera.append(pessoa[:])
print(galera)'''
'''pessoas = [['Felipe', 24], ['Daniel', 23], ['Bruno', 32], ['Caio', 46]]
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')
'''
pessoas = []
dados = []
for p in range(3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()
for p in pessoas:
    print(p[0].capitalize(), end='')
    print(f' tem {p[1]} anos de idade...\n')
