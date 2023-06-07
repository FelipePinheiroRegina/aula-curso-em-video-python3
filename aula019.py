'''alunos = {'nome':'Felipe', 'Idade': 24}
alunos['sexo'] = 'M'
print(f'O aluno {alunos["nome"]} tem {alunos["Idade"]} anos de idade, e é do sexo {alunos["sexo"]}')
del alunos['Idade']
print(alunos)

# Filmes
filmes = {'titulo': 'Star Wars', 'ano': '1977', 'diretor': 'George Lucas'}
print(filmes.values())
print(filmes.keys())
print(filmes.items())

for k, v in filmes.items():
    print(f'O item {k} é {v}')

locadora = [{'titulo': 'Star Wars', 'ano': '1977', 'diretor': 'George Lucas'},
            {'titulo': 'Avanger', 'ano': '2012', 'diretor': 'Joss Whedon'},
            {'titulo': 'Matrix', 'ano': '1999', 'diretor': 'Wachowski'}]
print(locadora[0]['titulo'])'''
'''pessoas = {'nome': 'Felipe', 'idade': 24}
print(pessoas["nome"])
pessoas["nome"] = "Gustavo" #Trocando os valores
print(pessoas["nome"])'''

'''estados = list()
estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'siglas': 'SP'}
estados.append(estado1)
estados.append(estado2)
print(estados[1]['siglas'])'''
estado = dict()
brasil = list()
for c in range(3):
    estado['uf'] = str(input('Digite o estado: '))
    estado['siglas'] = str(input('Digite a sigla: '))
    #brasil.append(estado[:]) em um dicionario nao se faz copia assim
    brasil.append(estado.copy()) #se faz assim
for e in brasil:
    for v in e.values():
        print(f'{v}')
    #for k, v in e.items():
        #print(f'O Uf é {k} e a sigla é {v}')
