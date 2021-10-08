#O módulo random é um módulo python que gera números pseudo-aleatórios, ele precisa ser importado para ser usado.
import random

print(random.random()) #A função random() gera um número aleatório entre 0.0 e 1.0

numero1 = random.random() * 100 #Podemos realizar operações
print(numero1)

numero2 = random.randrange(1, 51) #Essa função de random possibilita a definição do valor inicial e final a ser gerado
print(numero2)


