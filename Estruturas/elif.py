# O elif simplifica a criação de ifs encadeados em que cada um possui um bloco de código para uma condição

media_str = input("Digite sua média:\n")
media = float(media_str)

aprovado = media >= 7
recuperacao = media < 7 and media >= 5
final = media < 5 and media >= 3
if(aprovado):
    print("Sua média:", media, "Situação: Aprovado")
elif(recuperacao):
    print("Sua média:", media, "Situação: Recuperação")
elif(final):
    print("Sua média:", media, "Situação: Prova Final")
else:
    print("Reprovado")