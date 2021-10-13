#Tuplas são estruturas de dados (sequência) ordenada que armazenam diversos tipos de dados, diferente das listas as tuplas são imutáveis

dados_pessoais = ("Paulo", "02/04/1998", "Homem")
print(dados_pessoais) 

#podemos acessar os valores da tupla por meio do indice
print(dados_pessoais[1])

#Também é possível converter uma sequência mutável em imutável e o inverso

dados_pessoais_2 = ["Cleide", "28/04/1969", "Mulher"]

dados_pessoais_2_em_tupla = tuple(dados_pessoais_2)

#Podemos armazenar listas dentro de tuplas e outras estruturas de dados

dados_familia = [dados_pessoais, dados_pessoais_2_em_tupla]
print(dados_familia)

#Podemos também acessar dados de listas usando o indice combinado com as tuplas
print("Nome Filho: {} \nNome Mãe: {}".format(dados_familia[0][0], dados_familia[1][0]))