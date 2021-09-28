#A função print() é uma função de saída usada para imprimir algo
print("Hello Wolrd")

#Entre algumas funcionalidades podemos definir o tipo de separador de conteúdo e também o final da saída
print("Hello", "Wolrd", sep=" ", end="\n") #O padrão do separador é um espaço em branco e do final é pular para próxima linha

#Exemplo
print("Oi", "Eu", "sou", "o", "Goku", sep="_", end="!\n")

#Também podemos imprimir usando variáveis
nome = "Eduardo"
print("Meu nome e", nome)
idade = 23
print("Me chamo", nome, "eu tenho", idade, "anos!")

dia = 10
mes = 11
ano = 2021

print(dia, mes, ano, sep="/")