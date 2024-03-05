"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('insira um item: ')
        lista.append(valor)
        continue
    
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite um número inteiro')
        except IndexError:
            print('Índice inexistente')
        except Exception:
            print('Erro desconhecido')
        
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
        
    else:
        print('Por favor, escolha i, a ou l.')
