print("=================================")
print("Bem vindo ao jogo de Adivinhação!")
print("=================================")

numero_secreto = 20
chute_str = input("Qual o número secreto?\n")
chute = int(chute_str)

print("Você digitou:", chute)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
    print("Parabéns Você Acertou!")
else: 
    if(maior):
        print("O número que você digitou é maior que o número secreto!")
    elif(menor):
        print("O número que você digitou é menor que o número secreto!")
    else:
        print("Você Errou!")

print("Fim de Jogo!")