#A função input é usada para receber dados de entrada, retornando um tipo string e exibindo uma mensagem de saída
nome = input("Digite seu nome:\n")
idade = input("Digite sua idade:\n") #O input suporta caracteres de escape como por exemplo o \n
print(type(nome))
print(type(idade))

#Para converter o input em outro tipo podemos usar funções internas da linguagem como o int()