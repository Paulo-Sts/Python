# Operadores de identidade definem se um valor ou variável apontam para o mesmo endereço de memória (são o mesmo objeto) e retornam um booleano
nome1 = "Paulo"
nome2 = "Eduardo"

print(nome1 is "Paulo") # é o mesmo objeto
print(nome1 is nome1)
print(nome2 is nome1)
print(nome2 is not nome1) # não é o mesmo objeto