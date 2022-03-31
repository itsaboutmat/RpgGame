from time import sleep as ts
import os
from random import randrange as rr


def play():

    os.system('cls||clear')

    welcome_message()

    skip_tutorial()

    coin = 10
    escolha = historia_01()

    if escolha == 1:
        saiu_taverna(coin)
    elif escolha == 2:
        falou_com_dono_taverna(coin)
    elif escolha == 3:
        pediu_por_bebida(coin)
    elif escolha == 4:
        jogar_caneca(coin)

    #escolha = historia_02()

    #historia_02()

def welcome_message():
    print("#####################################################################################################")
    print("########################################  WELCOME TO MY GAME ########################################")
    print("#####################################################################################################",
          end='\n\n\n')
    ts(1.3)


def tutorial():
    line = "Bem vindo ao tutorial de XXXXXX. Aqui vão algumas informações básicas para você se familiarizar com o jogo."
    print(end='\n' * 4)
    tpsf(line)
    ts(1.5)
    line = "1- Este é um RPG onde suas decisões podem (e vão) alterar drasticamente a história dentro do jogo."
    print(end='\n\n')
    tpsf(line)
    print()
    input("Pressione ENTER")
    line = "2- Além de suas decisões, você contará com uma rolagem de um dado D20 influenciando o rumo da história."
    print(end='\n\n')
    tpsf(line)
    print()
    input("Pressione ENTER")
    line = "    Se tirar 1 no dado, você tirou um 'ERRO CRÍTICO', o que significa que algo bem ruim irá acontecer."
    print(end='\n\n')
    tpsf(line)
    print()
    input("Pressione ENTER")
    line = "    Se o seu resultado for um número entre 2 e 10, você tirou um número baixo demais, e podem"
    print(end='\n\n')
    tpsf(line)
    ts(1)
    line = "    acontecer coisas inexperadas com você pela jornada também, então torça pra tirar mais que 10!"
    print()
    tpsf(line)
    print()
    input("Pressione ENTER")
    line = "    Se conseguir um número entre 11 e 19 no dado, você conseguirá realizar a decisão que escolheu sem"
    print(end='\n\n')
    tpsf(line)
    ts(1)
    line = "    nenhum problema, e continuará pela história."
    print()
    tpsf(line)
    print()
    input("Pressione ENTER")
    line = "    Agora, se tirar um 20, aí você conseguiu um 'ACERTO CRÍTICO', na prática isso significa que não só"
    print(end='\n\n')
    tpsf(line)
    ts(1)
    line = "    você conseguiu fazer a ação que estava tentando, como também foi tão sortudo que conseguiu algo"
    print()
    tpsf(line)
    ts(1)
    line = "    a mais, como um diálogo secreto, uma pista sobre um personagem, ou até mesmo algum tesouro escondido."
    print()
    tpsf(line)
    print()
    input("Pressione ENTER")
    line = "3- Você inicia o jogo com 10 moedas, e conforme a história acontece, dependendo de suas decisões e da"
    print(end='\n\n')
    tpsf(line)
    ts(1)
    line = "rolagem de dados, você pode conseguir mais dinheiro, ou perder dinheiro, comprar itens que facilitarão sua"
    print()
    tpsf(line)
    ts(1)
    line = "jornada, ou ter que ir por um caminho mais difícil por não conseguir pagar alguém."
    print()
    tpsf(line)
    print()
    input("Pressione ENTER")
    line = "4- Existem diálogos secretos no game, que podem ser desbloqueados dependendo de alguns fatores que..."
    print(end='\n\n')
    tpsf(line)
    ts(1.7)
    line = "bom, você não achou MESMO que eu fosse te contar não é? Hahahahahaha"
    print()
    tpsf(line)
    print()
    input("Pressione ENTER")
    line = "Tente ser amigável com os NPCs... Ou não! É a sua jornada, e você decide como vai trilhá-la."
    print(end="\n\n")
    tpsf(line)
    ts(1)
    line = "Boa sorte, e divirta-se!!"
    print()
    tpsf(line)
    print()
    input("Pressione ENTER")
    line = "Quer reler o tutorial?"
    print(end="\n\n")
    tpsf(line)
    ts(.5)
    line = "(1) Reler o tutorial        (2) Ir para o jogo"
    print()
    tpsf(line)
    ts(1)
    resposta = int(input())

    if resposta == 1:
        tutorial()


def historia_01():
    line = "Você acorda em uma taverna."
    type_regular(line)
    line = "A música é alta, e o lugar está cheio."
    type_regular(line)
    line = "Sua cabeça dói enquanto você força para levantá-la da mesa."
    type_regular(line)
    line = "Ela parece pesada, por que será?"
    type_regular(line)
    line = "Sua visão está embaçada também."
    type_regular(line)
    line = "'Será que estou morto?'"
    print(end="\n\n")
    tpn(line)
    ts(.5)
    line = ". . ."
    print()
    type_regular(line)
    line = "'Não...'"
    print()
    type_regular(line)
    line = "Você pensa enquanto observa o lugar."
    print()
    type_regular(line)
    line = "Mesmo com todo o barulho, ainda dá para ouvir nitidamente música ali." \
           "Um bardo bêbado canta a plenos pulmões enquanto toca seu instrumento."
    type_regular(line)
    line = "- Droga, um bardo, eu odeio bardos..."
    print()
    type_regular(line)
    line = "O que você faz?"
    print()
    type_regular(line)
    print(end="\n")
    line = "(1) Sair da taverna     (2) Ir falar com o dono da taverna      (3) Gritar por uma bebida" \
           "    (4) Jogar uma caneca no bardo"
    print()
    tpsf(line)
    escolha = int(input("Sua escolha: "))
    print(end="\n")
    return escolha


def saiu_taverna(coin):

    # Erro Crítico no Dado
    def dado01(coin):
        line = "Ao dar o primeiro passo, tropeça em algo e imediatamente cai no chão"
        type_regular(line)
        line = "Quando olha no que tropeçou, se depara com uma mulher olhando furiosamente para você."
        type_regular(line)
        line = "- Você está de gracinha comigo? Acha que só porque sou mulher pode vir desse jeito é?"
        type_regular(line)
        line = "Antes que pudesse dizer qualquer coisa, ela dá um chute no seu estômago, e pega seu saco de moedas"
        print()
        type_regular(line)
        coin = coin - 10
        ts(1.5)
        line = "Você perdeu: 10 moedas."
        print(end="\n\n")
        tpf(line)
        ts(1.0)
        line = "Agora você tem ", coin, " moedas."
        tpf(line)
        ts(1.5)
        line = "A mulher sai bufando enquanto você se levanta segurando o estômago de dor."
        print()
        type_regular(line)

        return coin

    # Erro no Dado
    def dado02(coin):
        line = "- HEY!!!"
        print(end="\n\n")
        tpn(line)
        ts(.7)
        line = "Você ouve uma voz masculina berrar atrás de você."
        print()
        type_regular(line)
        line = "- Acha que vai sair sem me pagar? Você escolheu a taverna errada para beber de graça meu chapa"
        print()
        type_regular(line)
        line = "Vamos, me pague as 5 moedas que me deve e te deixo sair numa boa"
        type_regular(line)
        line = "Pagar as 5 moedas?"
        print()
        type_regular(line)
        line = "(1) Tentar Barganhar        (2) Pagar       (3) Dizer que não tem dinheiro"
        print()
        tpsf(line)
        ts(.5)
        print()

        escolha = int(input())

        # Escolheu Barganhar
        if escolha == 1:
            # Barganha
            def barganha():
                line = "- Será que poderia me dar um desconto? Eu ainda tenho que pagar pra dormir hoje a noite sabe."
                print()
                tpn(line)
                ts(.5)

            line = "Você vai ter que rolar um dado."
            type_regular(line)
            dado = rolar_d20()
            ts(1)

            # Erro Crítico no Dado
            if dado == 1:
                barganha()

                line = "- Desconto? HAHAHAHAHAHA. Tenta sair sem pagar e ainda quer desconto?"
                type_regular(line)
                line = "Agora são 10 MOEDAS que me deve. Tente barganhar de novo e eu ainda chamo os guardas"
                type_regular(line)

                # Se TEM moedas Suficientes
                if coin > 10:
                    coin = coin-10
                    line = "Você pagou 10 moedas para o dono da taverna"
                    type_regular(line)
                    line = "Agora você tem ", coin, " moedas"
                    type_regular(line)
                    print()
                    historia_02(coin)

                # Se NÃO tem moedas suficientes
                else:
                    line = "- Você está tirando uma com a minha cara? Você não tem moedas para me pagar"
                    type_regular(line)
                    line = "Seu total de moedas é de ", coin
                    type_regular(line)
                    line = "GUARDAS!! GUARDAS!!"
                    type_regular(line)
                    print()
                    nao_pagou(coin)

            # Erro no Dado
            elif dado > 1 and dado <= 10 :
                barganha()
                line = "- Não me venha com gracinhas, isso aqui não é uma caridade. Ande, pague minhas 5 moedas e dê"
                type_regular(line)
                line = "o fora daqui logo, antes que eu chame os guardas!"
                type_regular(line)

                # Se NÃO tem moedas suficientes
                if coin >= 5:
                    coin = coin-5
                    line = "Você pagou 5 moedas para o dono da taverna"
                    type_regular(line)
                    line = "Agora você tem ", coin, " moedas"
                    type_regular(line)
                    historia_02(coin)

                # Se TEM moedas suficientes
                else:
                    line = "- Você está tirando uma com a minha cara? Você não tem moedas para me pagar"
                    type_regular(line)
                    line = "Seu total de moedas é de ", coin
                    type_regular(line)
                    print()
                    nao_pagou(coin)

            # Acerto no Dado
            elif dado > 10 and dado <= 19:
                barganha()
                line = "- Ergh...Olha só, eu não quero encrenca, se prometer sair numa boa eu faço 3 moedas. "
                type_regular(line)
                line = "Temos um acordo?"
                type_regular(line)
                print()
                line = "Pagar agora?"
                type_super_fast(line)
                line = "(1) Sim         (02) Não"
                type_super_fast(line)

                pagou = int(input())

                if pagou == 1:
                    if coin < 3:
                        line = "- Você está tirando uma com a minha cara? Você não tem moedas para me pagar"
                        type_regular(line)
                        line = "Seu total de moedas é de ", coin
                        type_regular(line)
                        print()
                        nao_pagou(coin)

                    elif coin >= 3:
                        coin = coin-3
                        line = "Você pagou 5 moedas para o dono da taverna"
                        type_regular(line)
                        line = "Agora você tem ", coin, " moedas"
                        type_regular(line)
                        historia_02(coin)

                else:
                    line = "- Eu tento te ajudar e é assim que retribui? Minha mãe me disse que abrir uma taverna"
                    type_regular(line)
                    line = "não era uma boa ideia... GUARDAS!! GUARDAS!!"
                    type_regular(line)
                    nao_pagou(coin)

            # Acerto crítico no Dado
            elif dado == 20:
                barganha()
                line = "- Ergh... Na verdade ontem antes de beber até cair, você já tinha pago pelas bebidas"
                type_regular(line)
                line = "quis tentar ganhar um dinheiro a mais, porque com os impostos que o reino cobra, as coisas "
                type_regular(line)
                line = "estão ficando difíceis para um simples dono de taverna como eu."
                type_regular(line)
                line = "Pode ir garoto, me desculpe por isso."
                type_regular()
                print()
                historia_02(coin)

        # Escolheu Pagar
        elif escolha == 2:
            line = "- OK, eu pago, eu pago..."
            type_regular(line)
            line = ". . ."
            type_slow(line)

            if coin < 5:
                line = "Ahh, sabe o que é... na verdade eu não tenho nenhum dinheiro aqui comigo agora..."
                type_regular(line)
                line= "- Você acha que estou brincando garoto?"
                type_regular(line)
                line = "O dono da taverna chega mais perto. Ele é enorme, poderia te rasgar em dois se quisesse."
                type_regular(line)
                line = "- VOCÊ ACHA QUE ESTOU BRINCANDO?? GUARDAS!! GUARDAS!!"
                type_regular(line)
                nao_pagou(coin)

            elif coin >= 5:
                coin = coin-5
                line = "Você pagou 5 moedas ao dono da taverna"
                type_regular(line)
                line = "Você tem um total de ", coin, " moedas agora"
                type_regular(line)
                historia_02(coin)


        # Escolheu Dizer que não tem dinheiro
        elif escolha == 3:
            line = "Ahh, sabe o que é... na verdade eu não tenho nenhum dinheiro aqui comigo agora..."
            type_regular(line)
            line = "- Você acha que estou brincando garoto?"
            type_regular(line)
            line = "O dono da taverna chega mais perto. Ele é enorme, poderia te rasgar em dois se quisesse."
            type_regular(line)
            line = "- VOCÊ ACHA QUE ESTOU BRINCANDO?? GUARDAS!! GUARDAS!!"
            type_regular(line)
            print()
            nao_pagou(coin)

    # Acerto no Dado
    def dado03(coin):
        line = "Você se levanta. Agora consegue ver que a taverna está ainda mais cheia do que parecia."
        type_regular(line)
        line = "A porta está a direita, o taverneiro olha feio pra você e parece que grita algo, mas se esgueira"
        type_regular(line)
        line = "tão rápido que já está do lado de fora da taverna."
        type_regular(line)
        print()
        line = "- Arghh... "
        type_regular(line)
        line = "O sol brilha forte e machuca seus olhos enquanta você anda procurando uma sombra pra se proteger."
        type_regular(line)
        line = "- Eu deveria ter bebido menos ontem a noite, esse sol com a mimnha ressaca não é uma boa combinação"
        type_regular(line)
        line = "Depois de um tempo com seus olhos se acostumando com a claridade, você percebe uma figura encapuzada"
        type_regular(line)
        line = "próxima da porta da taverna. Ela parece estar te olhando. Não dá pra ter certeza já que mal é possível"
        type_regular(line)
        line = "enxergar o rosto embaixo do capuz."
        type_regular(line)
        line = "Você tenta ignorar, sai andando enquanto acelera o passo."
        type_regular(line)
        line = ". . ."
        type_slow(line)
        ts(1)
        line = "Vira uma esquina... Mais uma... Outra... E ao olhar pra trás... Sim, o sujeito de capuz está"
        type_regular(line)
        line = "realmente te seguindo."
        type_regular(line)
        print()
        line = "'O que será que esse esquisitão quer comigo?'"
        type_regular(line)
        print()
        line = "Você checa seus bolsos."
        type_regular(line)
        line = "Você tem ", coin, " moedas."
        type_regular(line)

        if coin == 0:
            print()
            line = "'Ótimo, nem pra ser roubado eu sirvo, nenhuma moeda nem pra dar esmola,, tenho que despistá-lo'"
            type_regular(line)
        else:
            print()
            line = "'Ótimo, vão roubar TODAS as minhas ", coin, " moedas. Mal tenho dinheiro pra mim, ainda vou perder"
            type_regular(line)
            line = "o que tenho.'"
            type_regular(line)

        print()
        line = "Você precisa despistá-lo, o que vai fazer?"
        type_super_fast(line)
        line = "(1) Correr          (2) Confrontar o estranho           (3) Se esconder"
        type_super_fast(line)
        print()
        escolha = int(input())
        print()

        if escolha == 1:
            line = "Você começa andar mais rápido. De repente está trotando. Quando menos percebe está correndo como"
            type_regular(line)
            line = "se sua vida dependesse disso. 'Talvez dependa'. Você pensa."
            type_regular(line)
            line = "Você correu vários metros, está sem fôlego e precisa parar. Mas e se o sujeito ainda estiver"
            type_regular(line)
            line = "atrás de você?"
            type_regular(line)
            print()
            line = "Olhar para trás?"
            type_super_fast(line)
            line = "(1) Sim         (2) Não"
            type_super_fast(line)
            print()
            escolha = int(input())
            print()

            if escolha == 1:
                line = "Não tem ninguém no seu campo de visão. Você conseguiu despistar o estranho."
                type_regular(line)
                print()
                line = ". . ."
                type_slow(line)
                ts(1)
                print()
                line = "Você respira mais aliviado. Já pode seguir seu caminho."
                type_regular(line)
                print()
                line = "- AAHHHHHHH!!!"
                type_regular(line)
                print()
                line = "O estranho está na sua frente, com o rosto quase encostando no seu."
                type_regular(line)
                print()
                line = "- Como você... O que você... Quem é... Olha, eu não tenho nada para ser roubado"
                type_regular(line)
                line = "Você acha que eu vou roubá-lo?"
                type_regular(line)
                line = "Ahh... Sim! Por que mais estaria me seguindo?"
                type_regular(line)


            else:
                pass

        elif escolha == 2:
            pass

        elif escolha == 3:
            pass

    # Acerto Crítico no Dado
    def dado04(coin):
        print("Você foi MUITO bem")

    line = "Você tenta sair da taverna e..."
    print(end="\n\n")
    tpn(line)
    line = "Rolar dados"
    print()
    tpn(line)
    print()
    input("Aperte ENTER")
    d20 = rolar_d20()
    if d20 == 1:
        dado01(coin)
    elif d20 > 1 and d20 <=10:
        dado02(coin)
    elif d20 > 10 and d20 <= 19:
        dado03(coin)
    elif d20 == 20:
        dado04(coin)

    return coin


def nao_pagou():
    pass

def falou_com_dono_taverna():
    pass

def pediu_por_bebida():
    pass

def jogar_caneca():
    pass

def historia_02(coin):
    pass

#Type Writer Super Fast
def tpsf(line):
    for char in line:
        ts(0.0005)
        print(char, end='', flush=True)
    print()

#Type Writer Fast
def tpf(line):
    for char in line:
        ts(0.001)
        print(char, end='', flush=True)
    print()

#Type Writer Normal
def tpn(line):
    for char in line:
        ts(0.04)
        print(char, end='', flush=True)
    print()

#Type Writer Slow
def tps(line):
    for char in line:
        ts(0.09)
        print(char, end='', flush=True)
    print()

# Type Writer Super Slow
def tpss(line):
    for char in line:
        ts(0.15)
        print(char, end='', flush=True)
    print()

def type_slow(line):
    print()
    tps(line)
    ts(.5)

def rolar_d20():
    d20 = rr(0, 21)
    print()
    print("Rolando dado...")
    ts(.5)
    if d20 == 1:
        line = ". . ."
        print()
        tpss(line)
        print()
        ts(.7)
        print("### ERRO CRÍTICO!!! ### VOCÊ TIROU {}".format(d20))
        ts(.5)
    elif d20 > 1 and d20 <20:
        line = ". . ."
        print()
        tpn(line)
        print()
        ts(.7)
        print("VOCÊ TIROU {}".format(d20))
        ts(.5)
    elif d20 == 20:
        line = ". . ."
        print()
        tpn(line)
        print()
        ts(.7)
        print("### ACERTO CRÍTICO!!! ### VOCÊ TIROU {}".format(d20))
        ts(.5)
    return d20

def type_regular(line):
    print()
    tpn(line)
    ts(.5)

def type_super_fast(line):
    print()
    tpsf(line)
    ts(.5)


def skip_tutorial():
    line = "Deseja ver o tutorial?"
    type_super_fast(line)
    line = "(1) Sim         (2) Não"
    type_super_fast(line)
    print()
    escolha = int(input())

    if escolha == 1:
        tutorial()

if __name__ == "__main__":
    play()