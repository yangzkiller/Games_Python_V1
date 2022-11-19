#GAME OF DIVINATION V2
#DATA: 09/05/22
#PROGRAMADOR: YANGZ
#ALTERAÇÃO: 19/08/2022

#CORES TERMINAL
reset = '\033[1;30m'
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'

#IMPORTAÇÃO DE GALERIA PRA ESCOLHER N ALEATORIO
#IMPORTAÇÃO DE GALERIA DE TEMPO'''
from random import randint
from time import sleep

#INICIAÇÃO DO JOGO
computador = randint(0, 10)
print(green, '-=-' * 20)
print(yellow, 'Sou seu computador... Acabei de pensar em um número entre 0 e 10!')
print(green, '-=-' * 20)
sleep(1)
print(yellow, 'Será que voce consegue adivinhar qual foi???')
print(green, '-=-' * 20)
sleep(1)

#VARIAVEIS
#ENTRADA DE DADOS
#LOOP DE PALPITE ATÉ O USUARIO ACERTA
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('\033[0;93mQual é seu palpite? \033[0;0m'))
    palpites += 1
    print(green, '-=-' * 20)
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print(red, 'Mais... Tente mais uma vez!')
        elif jogador > computador:
            print(red, 'Menos... Tente mais uma vez!')
print(green, 'ACERTOU! com {} Tentativas\033[0;0m'.format(palpites))
print(green, '-=-' * 20)