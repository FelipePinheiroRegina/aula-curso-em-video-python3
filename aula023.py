'''
try:
    a = int(input('Numerador: '))   # TENTE UMA OPERAÇÃO
    b = int(input('Divisor: '))
    r = a / b
except Exception as erro:   # Para identificar os tipos de erro
    print(f'ERRO DE EXCEÇÃO!, tipo do erro {erro.__class__}')   # SE OCORRER UMA EXCEÇÃO, OQ APARECERA PARA O USUARIO
else:
    print(f'{a} / {b} = {r}')   # CASO ESTEJA CERTO
finally:
    print('Volte sempre!')      # SEMPRE ACONTECE, FALHA/SUCESSO
'''
try:
    a = int(input('Numerador: '))   # TENTE UMA OPERAÇÃO
    b = int(input('Divisor: '))
    r = a / b
except (ValueError, TypeError):
    print('Erro com o tipo do dado informado!')    # SE OCORRER UMA EXCEÇÃO, OQ APARECERA PARA O USUARIO
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados')
else:
    print(f'{a} / {b} = {r}')   # CASO ESTEJA CERTO
finally:
    print('Volte sempre!')      # SEMPRE ACONTECE, FALHA/SUCESSO