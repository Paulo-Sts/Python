#Uma das formas de concatenar strings é por meio da função format()

nome = "Paulo"
idade = 23
profissao = "Programador"

print("Oi meu nome é {}, tenho {} anos e sou {}.".format(nome, idade, profissao))

#Podemos especificar qual a ordem de impressão dos valores

print("Oi meu nome é {0}, tenho {2} anos e sou {1}.".format(nome, idade, profissao))

#Podemos configurar a string de formatação como desejarmos

print("Valor: R$ {:f}".format(1.52)) #Adicionando casas decimais 
print("Valor: R$ {:.1f}".format(1.50)) #Limitando o número de casas decimais
print("Valor: R$ {:4.2f}".format(3900.000)) #Definindo o número de casas antes do ponto
print("Valor: R$ {:04.2f}".format(1.50)) #Adicionando o 0 no espaço vazio
print("Horário: {:02d}:{:0d}:{:0d}".format(2, 45, 59)) #Usando a formatação para números inteiros