# O while é uma estrutura que executa um bloco de código em loop enquanto uma condição é atendida
print("================")
print("RESULTADO PROVAS")
print("================")

notas = 1
total_notas = 0
while(notas <= 4): # No while os parenteses são opcionais
    recebe_nota_str = input("Digite sua nota:\n")
    nota = float(recebe_nota_str)
    total_notas = total_notas + nota
    
    notas = notas + 1
media = total_notas / 4
print("Sua média é: {}".format(media))