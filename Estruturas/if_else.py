#O if else define um bloco de código executável quando uma condição for verdadeira e outro caso ela seja falsa

idade_str = input("Digite sua idade:\n")
idade = int(idade_str)

maior = idade >= 18

if(maior):
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")