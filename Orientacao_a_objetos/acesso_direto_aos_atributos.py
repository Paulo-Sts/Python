class Livro:
    def __init__(self, nome, autor, preco):
        self.nome = nome
        self.autor = autor
        self.preco = preco


livro1 = Livro("A terra inabitável", "David Wallace-Wells", 45.50)
livro2 = Livro("Contos Inacabados", "J.R.R.Tolkien", 39.90)

#Podemos acessar os atributos via o operador ponto seguindo a sintaxe variável_referência.nome_atributo

print("Nome: {} Autor: {} Preço: {}".format(livro1.nome,livro1.autor, livro1.preco))
print("Nome: {} Autor: {} Preço: {}".format(livro2.nome,livro2.autor, livro2.preco))