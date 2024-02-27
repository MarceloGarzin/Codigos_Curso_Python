"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

Plv_secreta = 'carro'
letras_acertadas = ''
numero_tentativas = 0

while True: 
    letra_dgt = input('Digite uma letre: ')
    numero_tentativas += 1

    if len(letra_dgt) > 1:  
        print('Digite apenas uma letra')
        continue

    if letra_dgt in Plv_secreta:
        letras_acertadas += letra_dgt

    palavra_formada = ''
    for letra_secreta in Plv_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada: ', palavra_formada)

    if palavra_formada == Plv_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!!! PARABÉNS!!!')
        print('A PALAVRA ERA:', Plv_secreta)
        print('Tentativas: ', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
        


