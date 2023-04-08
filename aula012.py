nome = str(input('Digite seu nome: ')).strip().upper()
print('Bom dia!, {}'.format(nome))
if nome == 'FELIPE':
    print('Seu nome é muito bonito!')
elif nome == 'GUSTAVO' or nome == 'DANIEL' or nome == 'CAMILA':
    print('Seu nome é popular no Brasil!')
elif nome in 'ANA CAMILE PAULA JUDITE':
    print('Belo nome feminino')
else:
    print('Seu nome é tao normal!')
