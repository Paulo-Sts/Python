#O tipo string possui vários métodos que manipulam sequencias de caracteres e retornam uma nova string modificada

#Strings são sequências imutáveis, então quando uma string é manipulada por um método, ela não é modificada e sim o método retorna uma nova string

#Alguns exemplos
animal_1 = "cachorro"
animal_2 = "GATO"
animal_3 = "pASsArInHo"
animal_4 = "  Home m  "
print(animal_2.lower()) #Retorna todos os caracteres em minúsculo
print(animal_1.upper()) #Retorna todos os caracteres em maiúsculo
print(animal_3.capitalize()) #Retorna o primeiro caractere em maiúsculo e os demais em minúsculo
print(animal_4.strip()) #Retira os espaços vazios antes e depois da sequência
print(animal_3.find("n")) #Retorna a posição do caractere na palavra se ele existir
print(animal_2.startswith("G")) #Retorna um booleano se a sequência começar com determinado caractere
print(animal_4.endswith(" ")) #Retorna um booleano se a sequência terminar com determinado caractere