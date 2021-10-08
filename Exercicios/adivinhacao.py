import random
def jogar():
    print("=================================")
    print("Bem vindo ao jogo de Adivinhação!")
    print("=================================")

    numero_secreto = random.randrange(1, 101) #O valor final não entra na contagem
    total_tentativas = 0
    pontos = 1000

    print("Escolha o nível de dificuldade:")
    print("1: Fácil 2: Médio 3: Difícil")
    nivel = int(input("Qual nível de dificuldade você deseja?\n"))

    if nivel == 1:
        total_tentativas = 15
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for tentativa in range(1,total_tentativas + 1):
        print("Tentativa {} de {}".format(tentativa, total_tentativas))
        chute_str = input("Digite um número entre 1 e 100:\n")
        chute = int(chute_str)

        print("Você digitou:", chute)
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Sua pontuação foi de {} pontos".format(pontos))
            print("Parabéns Você Acertou!")
            break
        else: 
            if(maior):
                print("O número que você digitou é maior que o número secreto!")
                if (tentativa == total_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif(menor):
                print("O número que você digitou é menor que o número secreto!")
                if (tentativa == total_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            else:
                print("Você Errou!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de Jogo!")

if(__name__ == "__main__"):
    jogar()