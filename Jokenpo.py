#JOKENPO
#DATA: 09/05/22
#PROGRAMADOR: YANGZ
#ALTERAÇÃO: 19/08/2022

#CORES TERMINAL
reset = '\033[1;37m'
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
purple = '\033[1;35m'

#IMPORTAÇÃO GALERIA ALEATORIA
#IMPORTAÇÃO GALERIA DE TEMPO
from random import randint
from time import sleep

#VARIAVEIS
#ENTRADA DE DADOS
itens = ('\033[1;93mPEDRA', '\033[1;91mPAPEL', '\033[1;94mTESOURA')
computador = randint(0, 2)
print('''\033[4;92m\033[1;92mSuas opções: \033[0;90m
\033[1;93m[ 0 ] PEDRA
\033[1;91m[ 1 ] PAPEL
\033[1;94m[ 2 ] TESOURA''')
jogador = int(input('\033[4;92mQual é a sua jogada?\033[0;92m '))
print(yellow, 'JO')
sleep(1)
print(red, 'KEN')
sleep(1)
print(blue, 'PO!!!')
sleep(1)
print(green, '-=' * 11)
print('\033[4;92mComputador jogou\033[0;90m {}'.format(itens[computador]))
print('\033[4;92mJogador jogou\033[0;90m {}'.format(itens[jogador]))
print(green, '-=\033[90m' * 11)

#ESTRUTURAS CONDICIONAIS
if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('\033[1;92m\033[4;92mEMPATE')
    elif jogador == 1:
        print('\033[1;92m\033[4;92mJOGADOR VENCE')
    elif jogador == 2:
        print('\033[1;92m\033[4;92mCOMPUTADOR VENCE')

    else:
        print('\033[1;93m\033[4;93mJOGADA INVÁLIDA!')

elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('\033[1;92m\033[4;92mCOMPUTADOR VENCE')
    elif jogador == 1:
        print('\033[1;92m\033[4;92mEMPATE')
    elif jogador == 2:
        print('\033[1;92m\033[4;92mJOGADOR VENCE')
    else:
        print('\033[1;93m\033[4;93mJOGADA INVÁLIDA!')

elif computador == 2: #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('\033[1;92m\033[4;92mJOGADOR VENCE')
    elif jogador == 1:
        print('\033[1;92m\033[4;92mCOMPUTADOR VENCE')
    elif jogador == 2:
        print('\033[1;92m\033[4;92mEMPATE')
    else:
        print('\033[1;93m\033[4;93mJOGADA INVÁLIDA!')
