#JOGO DA VELHA
#DATA: 20/08/22
#PROGRAMADOR: YANGZ

#CORES TERMINAL
reset = '\033[1;37m'
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
purple = '\033[1;35m'

from random import randint
from time import sleep

#FUNÇÕES
def limparTela():
    print('\n'*100)

def cabecalho():
    print(yellow, '{:^50}'.format('=' * 50))
    print(blue, '{:^50}'.format('JOGO DA VELHA'))
    print(yellow, '{:^50}'.format('=' * 50))

def boasvindas():
    limparTela()
    cabecalho()
    print(blue, '{:^50}'.format('Bem-vindo ao jogo da velha'))
    print(yellow, '{:^50}'.format('-' * 50))

def placar(nomeP1, vitoriasP1, nomeP2, vitoriasP2, empates, simboloP1):
    limparTela()
    cabecalho()
    if simboloP1 == '1':
        simboloP1 = 'O'
        simboloP2 = 'X'
    elif simboloP1 == '2':
        simboloP1 = 'X'
        simboloP2 = 'O'
    print(blue, ' '*9, f'{nomeP1[0:15]:.<15}(\033[1;32m{simboloP1}\033[1;34m): \033[1;32m{vitoriasP1} Vitórias')
    print(blue, ' '*9, f'{nomeP2[0:15]:.<15}(\033[1;31m{simboloP2}\033[1;34m): \033[1;31m{vitoriasP2} Vitórias')
    print(yellow, ' '*9, f'                    {empates} Empates')
    print('{:^50}'.format('=' * 50))

def tabuleiro (c1, c2, c3, c4, c5, c6, c7, c8, c9):
    print(purple, '{:^19}'.format('      MAPA DO JOGO'))
    print(f'++=======++=======++=======++')
    print(f'||   {c1}   │|   {c2}   │|   {c3}   │|')
    print(f'++=======++=======++=======++')
    print(f'||   {c4}   │|   {c5}   │|   {c6}   │|')
    print(f'++=======++=======++=======++')
    print(f'│|   {c7}   │|   {c8}   │|   {c9}   │|')
    print(f'++=======++=======++=======++')     
    print()
    print(yellow, '{:^50}'.format('=' * 50))

def opcaoInicial():
    while True:
        boasvindas()
        print(blue, 'Escolha...\n'
              '\033[1;33m[0]\033[1;34m Para conhecer as regras\n'
              '\033[1;32m[1]\033[1;34m Para ser "\033[1;32m O \033[1;34m"\n'
              '\033[1;31m[2]\033[1;34m Para ser "\033[1;31m x \033[1;34m"\n')
        opcao = input('\033[1;34mQual a sua opção: ').strip()
        while opcao != '0' and opcao != '1' and opcao != '2':
            opcao = input('\033[1;31mOpção inválida. \033[1;34mQual a sua opção: [\033[1;33m0\033[1;34m/\033[1;32m1\033[1;34m/\033[1;31m2\033[1;34m] ').strip()
        if opcao == '0':
            regras()
        if opcao == '1' or opcao == '2':
            break
    return opcao

def opcaoPlayer():
    print(yellow, '--' * 50)
    print('\033[1;34mEscolha...\n'
          '\033[1;35m[\033[1;33m1\033[1;35m] para jogar contra o computador\n'
          '[\033[1;33m2\033[1;35m] para jogar contra outra pessoa\033[1;34m\n')
    opcao = input('Qual a sua opção: ').strip()
    while opcao != '1' and opcao != '2':
        opcao = input('\033[1;31mOpção inválida.\033[1;34m Qual a sua opção?\033[1;33m [1/2] ').strip()
    return opcao

def modoDificil():
    print()
    print(yellow, '-' * 50)
    print(blue, 'Deseja jogar em qual dificuldade: \n'
          '[\033[1;33m1\033[1;34m] \033[1;32mNormal\033[1;34m (movimentos aleatórios pc)\n'
          '[\033[1;33m2\033[1;34m] \033[1;31mDifícil\033[1;34m (movimentos do pc são calculados)')
    opcao = input('Qual a sua opção: ').strip()
    while opcao != '1' and opcao != '2':
        opcao = input('\033[1;31mOpção inválida.\033[1;34m Qual a sua opção?\033[1;33m [1/2] ').strip()
    if opcao == '1':
        return False
    else:
        return True

def verificarVencedor(c1, c2, c3, c4, c5, c6, c7, c8, c9):
    #VALIDAÇÃO LINHAS
    if c1 == c2 and c1 == c3 and c1 != ' ':
        return True
    elif c4 == c5 and c4 == c6 and c4 != ' ':
        return True
    elif c7 == c8 and c7 == c9 and c7 != ' ':
        return True
    #VALIDAÇÃO COLUNAS
    elif c1 == c4 and c1 == c7 and c1 != ' ':
        return True
    elif c2 == c5 and c2 == c8 and c2 != ' ':
        return True
    elif c3 == c6 and c3 == c9 and c3 != ' ':
        return True
    #VALIDAÇÃO DIAGONAIS
    elif c1 == c5 and c1 == c9 and c1 != ' ':
        return True
    elif c3 == c5 and c3 == c7 and c3 != ' ':
        return True
    else:
        return False

def verificarEmpate(c1, c2, c3, c4, c5, c6, c7, c8, c9):
    if c1 == ' ' or c2 == ' ' or c3 == ' ' or c4 == ' ' or c5 == ' ' or c6 == ' ' or c7 == ' ' or c8 == ' ' or c9 == ' ':
        return False
    elif verificarVencedor(c1, c2, c3, c4, c5, c6, c7, c8, c9):
        return False
    else:
        return True

def nivelDificil(c1, c2, c3, c4, c5, c6, c7, c8, c9, pc):
    if pc == 'o':
        adv = 'x'
    elif pc == 'x':
        adv = 'o'
    sugestao = 0
    listaOpcoes1 = []
    listaOpcoes2 = []
    listaOpcoes3 = []
    listaOpcoes4 = []
    listaOpcoes5 = []
    listaOpcoes6 = []
    #LISTA SUGESTÕES 1
    #VAI SUGERIR CASA 1
    if c1 == ' ':
        if c2 == pc and c3 == pc or c4 == pc and c7 == pc or c5 == pc and c9 == pc:
            listaOpcoes1.append(1)
    #VAI SUGERIR CASA 2
    if c2 == ' ':
        if c1 == pc and c3 == pc or c5 == pc and c8 == pc:
            listaOpcoes1.append(2)
    #VAI SUGERIR CASA 3
    if c3 == ' ':
        if c1 == pc and c2 == pc or c6 == pc and c9 == pc or c5 == pc and c7 == pc:
            listaOpcoes1.append(3)
    #VAI SUGERIR CASA 4
    if c4 == ' ':
        if c5 == pc and c6 == pc or c1 == pc and c7 == pc:
            listaOpcoes1.append(4)
    #VAI SUGERIR CASA 5
    if c5 == ' ':
        if c4 == pc and c6 == pc or c2 == pc and c8 == pc or c1 == pc and c9 == pc:
            listaOpcoes1.append(5)
    #VAI SUGERIR CASA 6
    if c6 == ' ':
        if c4 == pc and c5 == pc or c3 == pc and c9 == pc:
            listaOpcoes1.append(6)
    #VAI SUGERIR CASA 7
    if c7 == ' ':
        if c8 == pc and c9 == pc or c1 == pc and c4 == pc or c3 == pc and c5 == pc:
            listaOpcoes1.append(7)
    #VAI SUGERIR CASA 8
    if c8 == ' ':
        if c7 == pc and c9 == pc or c2 == pc and c5 == pc:
            listaOpcoes1.append(8)
    #VAI SUGERIR CASA 9
    if c9 == ' ':
        if c7 == pc and c8 == pc or c3 == pc and c6 == pc or c1 == pc and c5 == pc:
            listaOpcoes1.append(9)
    #LISTA SUGESTÕES 2
    #VAI SUGERIR CASA 1
    if c1 == ' ':
        if c2 == adv and c3 == adv or c4 == adv and c7 == adv or c5 == adv and c9 == adv:
            listaOpcoes2.append(1)
    if c2 == ' ':
        if c1 == adv and c3 == adv or c5 == adv and c8 == adv:
            listaOpcoes2.append(2)
    if c3 == ' ':
        if c1 == adv and c2 == adv or c6 == adv and c9 == adv or c5 == adv and c7 == adv:
            listaOpcoes2.append(3)
    if c4 == ' ':
        if c5 == adv and c6 == adv or c1 == adv and c7 == adv:
            listaOpcoes2.append(4)
    if c5 == ' ':
        if c4 == adv and c6 == adv or c2 == adv and c8 == adv or c1 == adv and c9 == adv:
            listaOpcoes2.append(5)
    if c6 == ' ':
        if c4 == adv and c5 == adv or c3 == adv and c9 == adv:
            listaOpcoes2.append(6)
    if c7 == ' ':
        if c8 == adv and c9 == adv or c1 == adv and c4 == adv or c3 == adv and c5 == adv:
            listaOpcoes2.append(7)
    if c8 == ' ':
        if c7 == adv and c9 == adv or c2 == adv and c5 == adv:
            listaOpcoes2.append(8)
    if c9 == ' ':
        if c7 == adv and c8 == adv or c3 == adv and c6 == adv or c1 == adv and c5 == adv:
            listaOpcoes2.append(9)
    #LISTA DE SUGESTÕES 3
    #VAI SUGERIR CASA 1
    if c1 == ' ':
        if c2 == pc and c3 == ' ' or c3 == pc and c2 == ' ':
            listaOpcoes3.append(1)
        if c4 == pc and c7 == ' ' or c7 == pc and c4 == ' ':
            listaOpcoes3.append(1)
        if c5 == pc and c9 == ' ' or c9 == pc and c5 == ' ':
            listaOpcoes3.append(1)
    #VAI SUGERIR CASA 2
    if c2 == ' ':
        if c1 == pc and c3 == ' ' or c3 == pc and c1 == ' ':
            listaOpcoes3.append(2)
        if c5 == pc and c8 == ' ' or c8 == pc and c5 == ' ':
            listaOpcoes3.append(2)
    #VAI SUGERIR  CASA 3
    if c3 == ' ':
        if c1 == pc and c2 == ' ' or c2 == pc and c1 == ' ':
            listaOpcoes3.append(3)
        if c6 == pc and c9 == ' ' or c9 == pc and c6 == ' ':
            listaOpcoes3.append(3)
        if c5 == pc and c7 == ' ' or c7 == pc and c5 == ' ':
            listaOpcoes3.append(3)
    #VAI SUGERIR CASA 4
    if c4 == ' ':
        if c5 == pc and c6 == ' ' or c6 == pc and c5 == ' ':
            listaOpcoes3.append(4)
        if c1 == pc and c7 == ' ' or c7 == pc and c1 == ' ':
            listaOpcoes3.append(4)
    #VAI SUGERIR CASA 5
    if c5 == ' ':
        if c4 == pc and c6 == ' ' or c6 == pc and c4 == ' ':
            listaOpcoes3.append(5)
        if c2 == pc and c8 == ' ' or c8 == pc and c2 == ' ':
            listaOpcoes3.append(5)
        if c3 == pc and c7 == ' ' or c7 == pc and c3 == ' ':
            listaOpcoes3.append(5)
    #VAI SUGERIR CASA 6
    if c6 == ' ':
        if c4 == pc and c5 == ' ' or c5 == pc and c4 == ' ':
            listaOpcoes3.append(6)
        if c3 == pc and c9 == ' ' or c9 == pc and c3 == ' ':
            listaOpcoes3.append(6)
    #VAI SUGERIR CASA 7
    if c7 == ' ':
        if c8 == pc and c9 == ' ' or c9 == pc and c8 == ' ':
            listaOpcoes3.append(7)
        if c1 == pc and c4 == ' ' or c4 == pc and c1 == ' ':
            listaOpcoes3.append(7)
        if c3 == pc and c5 == ' ' or c5 == pc and c3 == ' ':
            listaOpcoes3.append(7)
    #VAI SUGERIR CASA 8
    if c8 == ' ':
        if c7 == pc and c9 == ' ' or c9 == pc and c7 == ' ':
            listaOpcoes3.append(8)
        if c2 == pc and c5 == ' ' or c5 == pc and c2 == ' ':
            listaOpcoes3.append(8)
    #VAI SUGERIR CASA 9
    if c9 == ' ':
        if c7 == pc and c8 == ' ' or c8 == pc and c7 == ' ':
            listaOpcoes3.append(9)
        if c3 == pc and c6 == ' ' or c6 == pc and c3 == ' ':
            listaOpcoes3.append(9)
        if c1 == pc and c5 == ' ' or c5 == pc and c1 == ' ':
            listaOpcoes3.append(9)
    #LISTA DE SUGESTÕES 4
    #VAI SUGERIR CASA 5
    if c5 == ' ':
        if c1 == adv or c3 == adv or c7 == adv or c9 == adv:
            listaOpcoes4.append(5)
    #LISTA DE SUGESTÕES 5
    #VAI SUGERIR CASAS 1, 3, 7 OU 9
    if c1 == ' ':
        listaOpcoes5.append(1)
    if c3 == ' ':
        listaOpcoes5.append(3)
    if c7 == ' ':
        listaOpcoes5.append(7)
    if c9 == ' ':
        listaOpcoes5.append(9)
    #LISTA SUGESTÕES 6
    if c1 == ' ':
        listaOpcoes6.append(1)
    if c2 == ' ':
        listaOpcoes6.append(2)
    if c3 == ' ':
        listaOpcoes6.append(3)
    if c4 == ' ':
        listaOpcoes6.append(4)
    if c5 == ' ':
        listaOpcoes6.append(5)
    if c6 == ' ':
        listaOpcoes6.append(6)
    if c7 == ' ':
        listaOpcoes6.append(7)
    if c8 == ' ':
        listaOpcoes6.append(8)
    if c9 == ' ':
        listaOpcoes6.append(9)
    #SUGERIR NÚMERO COM BASE NA SITUAÇÃO DO GAME
    if len(listaOpcoes1) > 0:
        sugestao = listaOpcoes1[randint(0, len(listaOpcoes1)-1)]
    elif len(listaOpcoes2) > 0:
        sugestao = listaOpcoes2[randint(0, len(listaOpcoes2)-1)]
    elif len(listaOpcoes3) > 0:
        sugestao = listaOpcoes3[randint(0, len(listaOpcoes3)-1)]
    elif len(listaOpcoes4) > 0:
        sugestao = listaOpcoes4[randint(0, len(listaOpcoes4)-1)]
    elif len(listaOpcoes5) > 0:
        sugestao = listaOpcoes5[randint(0, len(listaOpcoes5)-1)]
    else:
        sugestao = listaOpcoes6[randint(0, len(listaOpcoes6)-1)]

    return sugestao

def regras():
    limparTela()
    cabecalho()
    print('|{:^48}|'.format('\033[1;35mREGRAS DO JOGO'))
    print('{:^50}'.format('\033[1;33m-' * 50))
    print(purple, '{:^19}'.format('\033[1;35m      MAPA DO JOGO'))
    print(f'++=======++=======++=======++')
    print(f'||   \033[1;32m1\033[1;35m   │|   \033[1;32m2\033[1;35m   │|   \033[1;32m3\033[1;35m   │|')
    print(f'++=======++=======++=======++')
    print(f'||   \033[1;32m4\033[1;35m   │|   \033[1;32m5\033[1;35m   │|   \033[1;32m6\033[1;35m   │|')
    print(f'++=======++=======++=======++')
    print(f'│|   \033[1;32m7\033[1;35m   │|   \033[1;32m8\033[1;35m   │|   \033[1;32m9\033[1;35m   │|')
    print(f'++=======++=======++=======++')     
    print("""
- O tabuleiro  é uma matriz  de três linhas por
três colunas.
- Dois jogadores escolhem uma marcação cada um,
geralmente um círculo (o) e um xis (x).
- Os jogadores jogam alternadamente, uma marcação
por vez, numa lacuna que esteja vazia.
- O objectivo é conseguir três círculos ou três
xis em linha, quer horizontal, vertical ou
diagonal , e ao mesmo tempo, quando possível,
impedir o adversário de ganhar na próxima jogada.
Pronto para jogar?
""")
    input('\033[1;34mTecle enter para continuar!')

def dica():
    print("""\033[1;35mDica:\033[1;34m Para jogar, escolha o número de uma casa que
      esteja disponível no tabuleiro da direita.
\033[1;35mDigite: \033[1;32mnovo \033[1;34m Para reiniciar a rodada atual.
\033[1;35mDigite: \033[1;32mtrocar \033[1;34m Para novos jogadores.
\033[1;35mDigite: \033[1;32mzerar \033[1;34m Para zerar o placar.
\033[1;35mDigite: \033[1;32msair \033[1;34m Para encerrar o aplicativo.""")
    print('{:^50}'.format('\033[1;33m=' * 50))

#EXECUÇÃO
jogada = ''
while True:
    #INICIO VARIAVEIS DO GAME
    nomeP1 = ''
    nomeP2 = ''
    simboloP1 = ''
    simboloP2 = ''
    vitoriasP1 = 0
    vitoriasP2 = 0
    empates = 0
    proximoJogador = ''
    #VARIAVEIS TABULEIRO
    c1 = ' '
    c2 = ' '
    c3 = ' '
    c4 = ' '
    c5 = ' '
    c6 = ' '
    c7 = ' '
    c8 = ' '
    c9 = ' '

    opcaoUsuario = opcaoInicial()
    nomeP1 = input('Qual o seu nome? ')
    if opcaoUsuario == '1':
        simboloP1 = 'o'
        simboloP2 = 'x'
    elif opcaoUsuario == '2':
        simboloP1 = 'x'
        simboloP2 = 'o'

    jogadores = opcaoPlayer()
    if jogadores == '2':
        nomeP2 = input('Qual o nome do segundo jogador? ')
    else:
        dificil = modoDificil()
        nomeP2 = 'Computador'

    while True:
        if jogada == 'sair':
            break
        elif jogada == 'trocar':
            jogada = ''
            break
        elif jogada == 'novo':
            c1 = ' '
            c2 = ' '
            c3 = ' '
            c4 = ' '
            c5 = ' '
            c6 = ' '
            c7 = ' '
            c8 = ' '
            c9 = ' '
        elif jogada == 'zerar':
            vitoriasP1 = 0
            vitoriasP2 = 0
            empates = 0
            # VARIAVEIS CAMPOS TABULEIRO
            c1 = ' '
            c2 = ' '
            c3 = ' '
            c4 = ' '
            c5 = ' '
            c6 = ' '
            c7 = ' '
            c8 = ' '
            c9 = ' '

        placar(nomeP1, vitoriasP1, nomeP2, vitoriasP2, empates, opcaoUsuario)
        tabuleiro(c1, c2, c3, c4, c5, c6, c7, c8, c9)
        dica()

        if proximoJogador == '' or proximoJogador == nomeP2:
            proximoJogador = nomeP1
            proximoSimbolo = simboloP1
        else:
            proximoJogador = nomeP2
            proximoSimbolo = simboloP2

        while True:
            if jogadores == '1' and proximoJogador == 'Computador':
                if dificil:
                    jogada = str(nivelDificil(c1, c2, c3, c4, c5, c6, c7, c8, c9, simboloP2))
                else:
                    jogada = str(randint(1, 9))
            else:
                jogada = input(f'É a vez do {proximoJogador}({proximoSimbolo}): ').strip().lower()
            if jogada == 'sair' or jogada == 'trocar' or jogada == 'zerar' or jogada == 'novo':
                break
            if jogada.isnumeric():
                if int(jogada) >= 1 or int(jogada) <= 9:
                    if jogada == '1' and c1 == ' ':
                        c1 = proximoSimbolo
                        break
                    elif jogada == '2' and c2 == ' ':
                        c2 = proximoSimbolo
                        break
                    elif jogada == '3' and c3 == ' ':
                        c3 = proximoSimbolo
                        break
                    elif jogada == '4' and c4 == ' ':
                        c4 = proximoSimbolo
                        break
                    elif jogada == '5' and c5 == ' ':
                        c5 = proximoSimbolo
                        break
                    elif jogada == '6' and c6 == ' ':
                        c6 = proximoSimbolo
                        break
                    elif jogada == '7' and c7 == ' ':
                        c7 = proximoSimbolo
                        break
                    elif jogada == '8' and c8 == ' ':
                        c8 = proximoSimbolo
                        break
                    elif jogada == '9' and c9 == ' ':
                        c9 = proximoSimbolo
                        break
                    else:
                        if jogadores == '2':
                            print('Opção inválida, por favor escolha uma casa que esteja disponível e digite seu número!')
                else:
                    if jogadores == '2':
                        print('Opção inválida, por favor escolha uma casa que esteja disponível e digite seu número!')
            else:
                if jogadores == '2':
                    print('Opção inválida, por favor escolha uma casa que esteja disponível e digite seu número!')

        if jogadores == '1' and proximoJogador == 'Computador':
            print('O computador está jogando, por favor aguarde!')
            sleep(3)


        if verificarVencedor(c1, c2, c3, c4, c5, c6, c7, c8, c9):
            if proximoJogador == nomeP1:
                vitoriasP1 += 1
            else:
                vitoriasP2 += 1
            placar(nomeP1, vitoriasP1, nomeP2, vitoriasP2, empates, opcaoUsuario)
            tabuleiro(c1, c2, c3, c4, c5, c6, c7, c8, c9)
            if jogadores == '1' and proximoJogador == nomeP2:
                print('Que pena! Você perdeu!')
            else:
                print(f'Parabéns {proximoJogador}({proximoSimbolo}), você venceu!')
            opcao = input('Deseja continuar jogando? [S/N] ').strip().upper()
            while opcao != 'S' and opcao != 'N':
                opcao = input('Opção inválida! Deseja continuar jogando? [S/N] ').strip().upper()
            if opcao == 'S':
                jogada = 'novo'
            else:
                jogada = 'sair'
        elif verificarEmpate(c1, c2, c3, c4, c5, c6, c7, c8, c9):
            empates += 1
            placar(nomeP1, vitoriasP1, nomeP2, vitoriasP2, empates, opcaoUsuario)
            tabuleiro(c1, c2, c3, c4, c5, c6, c7, c8, c9)
            print('Essa rodada empatou!!')
            opcao = input('Deseja continuar jogando? [S/N] ').strip().upper()
            while opcao != 'S' and opcao != 'N':
                opcao = input('Opção inválida! Deseja continuar jogando? [S/N] ').strip().upper()
            if opcao == 'S':
                jogada = 'novo'
            else:
                jogada = 'sair'

    if jogada == 'sair':
        print('='*50)
        print('Obrigado por jogar!!!Espero que tenha gostado!!!')
        print('='*50)
        break




