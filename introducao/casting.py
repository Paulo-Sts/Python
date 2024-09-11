# Por meio de funções internas da linguagem podemos converter um tipo de dado em outro
# Principais funções de casting: int(), float(), str()

# Exemplos
valor_1 = 3
valor_2 = 2.89
valor_3 = "2.500"

print(valor_1,"é do tipo:",type(valor_1))
print(valor_2,"é do tipo:",type(valor_2))
print(valor_3, "é do tipo:",type(valor_3))

novo_valor_1 = str(valor_1)
novo_valor_2 = int(valor_2)
novo_valor_3 = float(valor_3)

print(novo_valor_1,"é do tipo:",type(novo_valor_1))
print(novo_valor_2,"é do tipo:",type(novo_valor_2))
print(novo_valor_3,"é do tipo:",type(novo_valor_3))