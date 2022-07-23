# Uma lista é uma sequência de valores ordenada, que possuem uma posição definida e um dado
# Em python lista podem ter valores de diferentes tipos, embora não seja recomendado a mistura de tipos diferentes

primeira_lista = [1, "Oi", True, 2.98]

print("oi" in primeira_lista) # Por meio do in podemos percorrer uma lista e verificar a existência de um valor dentro dela.

# Listas possuem funções e métodos que podemos usar para manipular seus valores
numeros = [20, 30, 40, 50, 60]
letras = ["a", "b", "a", "d", "a", "f", "w"]

numeros.append(70) # Método que adiciona valor a lista
print(numeros)

print(min(numeros)) # Retorna o menor valor da lista
print(max(numeros)) # Retorna o maior valor da lista

print(letras.count("a")) # Retorna a quantidade de vezes que um valor se encontra na lista

print(len(letras)) # Retorna o tamanho da lista

# Podemos converter sequências imutáveis como strings em listas
nome = "Catarina"
lista_nome = list(nome)
print(lista_nome)