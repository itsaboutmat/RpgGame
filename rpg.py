from time import sleep as ts
import os
from random import randrange as rr

def play():

    os.system('cls||clear')

    welcome()

    coin = 10
    escolha = historia_01()

    if escolha == 1:
        print("Escolha numero 1")
        saiu_taverna(coin)
    elif escolha == 2:
        falou_com_dono_taverna()
    elif escolha == 3:
        pediu_por_bebida()
    elif escolha == 4:
        jogar_caneca()

    #    escolha = historia_02()

def welcome():
    print("#####################################################################################################")
    print("########################################  WELCOME TO MY GAME ########################################")
    print("#####################################################################################################",end='\n\n\n')
    ts(1.3)

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
    line = "Mesmo com todo o barulho, ainda dá para ouvir nitidamente música ali."
    type_regular(line)
    line = "Um bardo bêbado canta a plenos pulmões enquanto toca seu instrumento."
    type_regular(line)
    line = "- Droga, um bardo, eu odeio bardos..."
    print()
    type_regular(line)
    line = "O que você faz?"
    print()
    type_regular(line)
    print(end="\n")
    line = "(1) Sair da taverna     (2) Ir falar com o dono da taverna      (3) Gritar por uma bebida"
    print()
    tpsf(line)
    line = "(4) Jogar uma caneca no bardo"
    print()
    tpsf(line)
    print()
    escolha = int(input())
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

        dado02(coin)

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
        line = "- Vamos, me pague as 5 moedas que me deve e te deixo sair numa boa"
        type_regular(line)
        line = "Pagar as 5 moedas?"
        print()
        type_regular(line)
        line = "(1) Tentar Barganhar        (2) Pagar       (3) Dizer que não tem dinheiro"
        print()
        tpsf(line)
        ts(.5)

        escolha = int(input())

        # Tentou Barganhar
        if escolha == 1:
            def barganha():
                line = "- Será que poderia me dar um desconto? Eu ainda tenho que pagar pra dormir hoje a noite sabe."
                print()
                tpn(line)
                ts(.5)

            line = "Você vai ter que rolar um dado."
            type_regular(line)
            dado = rolar_d20()
            ts(1)

            # Barganha
            # Erro Crítico no Dado
            if dado == 1:
                barganha()

                line = "Desconto? HAHAHAHAHAHA. Tenta sair sem pagar e ainda quer desconto?"
                type_regular(line)
                line = "Agora são 10 MOEDAS que me deve. Tente barganhar de novo e eu ainda chamo os guardas"
                type_regular(line)

                # Se tem moedas Suficientes
                if coin > 10:
                    coin = coin-10
                    line = "Você pagou 10 moedas para o dono da taverna"
                    type_regular(line)
                    line = "Agora você tem ", coin, " moedas"
                    historia_02(coin)
                # Se NÃO tem moedas suficientes
                else:
                    nao_pagou()
                return coin

            # Erro no Dado
            elif dado > 1 and dado <= 10:
                barganha()
                line = "Não me venha com gracinhas, isso aqui não é uma caridade. Ande, pague minhas 5 moedas e dê"
                type_regular(line)
                line = "o fora daqui logo, antes que eu chame os guardas!"
                type_regular(line)

                if coin >= 5:
                    coin = coin-5
                line = "Você pagou 5 moedas para o dono da taverna"
                type_regular(line)
                line = "Agora você tem ", coin, " moedas"
                type_regular(line)
                historia_02()
                return coin

                elif coin < 5:
                    line = "Você não tem moedas suficientes para pagar o dono da taverna"
                    type_regular(line)
                    line = "Seu total de moedas é de ", coin
                    type_regular(line)
                    nao_pagou()
                return coin
            # Acerto no Dado
            elif dado > 10 and dado <= 19:
                barganha()
                line = "Olha só, eu não quero encrenca, se prometer sair numa boa eu faço 3 moedas. Temos um acordo?"
                type_regular(line)
                line = "Pagar agora?"
                type_regular(line)
                line = "(1) Sim         (02) Não"
                type_regular(line)

                pagou = int(input())

                if pagou == 1:
                    coin = coin-3
                else:
                    nao_pagou()
            # Acerto crítico no Dado
            elif dado == 20:
                barganha()
                line = "Na verdade ontem antes de beber até cair, você já tinha pago pelas bebidas, quis tentar"
                type_regular(line)
                line = "ganhar um dinheiro a mais, porque com os impostos que o reino cobra, as coisas estão ficando"
                type_regular(line)
                line = "difíceis para um simples dono de taverna como eu. Pode ir garoto, me desculpe por isso."

        elif escolha == 2:
            pass

        elif escolha == 3:
            pass

    # Acerto no Dado
    def dado03(coin):
        print("Você foi bem")

    # Acerto Crítico no Dado
    def dado04(coin):
        print("Você foi MUITO bem")

    line = "Você tenta sair da taverna e..."
    print(end="\n\n")
    tpn(line)
    line = "Rolar dados"
    print()
    tpn(line)
    input()
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

def historia_02():
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

def rolar_d20():
    d20 = rr(0,21)
    print("Rolando dado...")
    ts(.5)
    if d20 == 1:
        line = ". . ."
        print()
        tpss(line)
        print()
        print("### ERRO CRÍTICO!!! ### VOCÊ TIROU {}".format(d20))
        ts(.5)
    elif d20 > 1 and d20 <20:
        line = ". . ."
        print()
        tpn(line)
        print()
        print("VOCÊ TIROU {}".format(d20))
        ts(.5)
    elif d20 == 20:
        line = ". . ."
        print()
        tpn(line)
        print()
        print("### ACERTO CRÍTICO!!! ### VOCÊ TIROU {}".format(d20))
        ts(.5)
    return d20

def type_regular(line):
    print()
    tpn(line)
    ts(.5)


if(__name__ == "__main__"):
    play()