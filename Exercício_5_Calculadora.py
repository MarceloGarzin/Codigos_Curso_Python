""" Calculadora com while """

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador (+-/*): 1')

    numeros_validos = None
    num_1float = 0
    num_2float = 0

    try:
        num_1float = float(numero_1)
        num_2float = float(numero_2)
        numeros_validos = True
  
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados sao invalidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inváido.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '+':
        resultado = num_1float + num_2float
        print(resultado)

    elif operador == '-':
        resultado = num_1float - num_2float
        print(resultado)
        
    elif operador == '/':
        resultado = num_1float / num_2float
        print(resultado)
        
    elif operador == '*':
        resultado = num_1float * num_2float
        print(resultado)

    else:
        print('erro') 

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break