import adivinhacao #Importa como módulo o arquivo adivinhacao.py
import forca #Importa como módulo o arquivo forca.py

print("===========================")
print("======Escolha o jogo!======")
print("===========================")

print("1: Forca 2: Adivinhação")
jogo = int(input("Qual jogo você quer?"))

if(jogo == 1):
    print("Jogando jogo da Forca")
    forca.jogar() #Chama a função jogar do arquivo forca.py
if(jogo == 2):
    print("Jogando jogo de adivinhação")
    adivinhacao.jogar() #Chama a função jogar do arquivo adivinhacao.py

