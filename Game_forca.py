6#GAME FORCA
#DATA:18/08/2022
#PROGRAMADOR: YANGZ
#ALTERAÇÃO: 20/08/2022

#CORES TERMINAL
reset = '\033[1;30m'
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'

from time import sleep
import getpass

#VARIAVEIS
secreto = ''
digitadas = []
chances = 3

#ENUNCIADO
print(yellow, '-=' * 20)
print(blue, '          JOGO DA FORCA')
print(yellow, '-=' * 20)
sleep(1)
secreto = getpass.getpass('\033[1;34mQual será a palavra secreta: ')
sleep(1)

#LAÇO - OQ O J VAI JOGAR
while True:
    letra = str(input('\033[1;94mDigite uma letra: '))
    print(yellow, '-=' * 20)

    #CASO O J JOGUE + DE UMA LETRA
    if len(letra)> 1:
        print(red, 'ERRO!!! Não vale digitar mais de uma letra!!!')
        sleep(1)
        continue

    #INSERE UM REGISTRO APÓS O ULTIMO ELEMENTO
    digitadas.append(letra)

    #PARA CADA LETRA PERTENCENTE A SECRETA IREMOS CHECAR SE ELA ESTÁ DIGITADA.
    #SE SIM UMA PALAVRA  CHAVE NA LISTA SECRETA_TEMPORARIO RECEBERA COMO LETRAS SECRETAS DIGITADAS PELO JOGADOR.
    #CASO NÃO EXIBIRA UM *
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '\033[1;91m*'

    #VERIFICAR SE UMA VARIAVEL SECRETO_TEMPORARIO É A PALAVRA SECRETA.
    #SEJA IGUAL EXIBE A VITORIA, SENÃO MOSTTARA QUANTO A FORMA SECRETA
    if secreto_temporario == secreto:
        sleep(1)
        print(green, f'Voce venceu a palavra é: {secreto}, PARABÉNS!!!')
        print(yellow, '-=' * 20)
        break
    else:
        print(blue, f'A palavra secreta está assim: \033[1;92m{secreto_temporario}')

    #LÓGICA DO CONTADOR DE CHANCES   
    if letra not in secreto:
        chances -= 1
    
    #CONDIÇÃO DE DERROTA
    if chances <= 0:
        sleep(1)
        print(red, f'Voce perdeu! A palavra era \033[1;32m({secreto})\033[1;31m !!!FORCA!!!')
        print(yellow, '-=' * 20)
        break

    #CHANCES QUE O USUARIO POSSUI
    print(yellow, f'Voce tem {chances} chances! ')
    print()
