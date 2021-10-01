print("=================================")
print("Bem vindo ao jogo de Adivinhação!")
print("=================================")

numero_secreto = 20
chute_str = input("Qual o número secreto?\n")
chute = int(chute_str)

print("Você digitou:", chute)

if(chute == numero_secreto):
    print("Parabéns Você Acertou!")
else:
    print("Você Errou!")

print("Fim de Jogo!")