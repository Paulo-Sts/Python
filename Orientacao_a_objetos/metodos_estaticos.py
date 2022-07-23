# São métodos que pertencem a classe independente da existencia de objetos. Para todos os objetos eles serão o mesmo
class Livro:
    def __init__(self, nome, autor, preco):
        self.__nome = nome
        self.__autor = autor
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome

    @staticmethod #Usa-se essa palavra reervada para definir um método estático
    def livraria():
        return "Saraiva"