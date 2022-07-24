# Em python, funções são definidadas com a palavra def

def imprime_nome():
    return print("Paulo")


imprime_nome()

# Podemos definir parâmetros

def boas_vindas(nome):
    return print("Olá {}, seja bem vindo".format(nome))

boas_vindas("Paulo")

# Que podem receber valores padrão

def boas_vindas(nome = "Paulo"):
    return print("Olá {}, seja bem vindo".format(nome))

boas_vindas()