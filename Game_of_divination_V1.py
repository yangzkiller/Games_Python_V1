#GAME OF DIVINATION V1
#DATA: 06/05/22
#PROGRAMADOR: YANGZ

#IMPORTAÇÃO DE GALERIA PRA ESCOLHER N ALEATORIO
#IMPORTAÇÃO DE GALERIA DE TEMPO
from random import randint
from time import sleep

#FAZ O COMPUTADOR RANDOMIZAR UM N DE 0 A 5
#ENTRADA DE DADOS DO USUARIO
computador = randint(0, 5)
print('-=-' * 20)
print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 5. TENTE ADIVINHAR...')
print('-=-' * 20)
jogador = int(input('EM QUE NÚMERO EU PENSEI? '))
print('PROCESSANDO...')
sleep(1)

#ESTRUTURA CONDICIONAL
if jogador == computador:
    print('PARABÉNS! VOCE CONSEGUIU ME VENCER')
else:
    print('GANHEI! EU PENSEI NO NÚMERO {} E NÃO NO {}!'.format(computador, jogador))