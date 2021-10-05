print("=================================")
print("Bem vindo ao jogo de Adivinhação!")
print("=================================")

numero_secreto = 20
total_tentativas = 3
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
        print("Parabéns Você Acertou!")
        break
    else: 
        if(maior):
            print("O número que você digitou é maior que o número secreto!")
        elif(menor):
            print("O número que você digitou é menor que o número secreto!")
        else:
            print("Você Errou!")

print("Fim de Jogo!")