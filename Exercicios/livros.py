class Livro:
    def __init__(self, titulo, ano, paginas):
        self._titulo = titulo.title()
        self.ano = ano
        self.paginas = paginas
        self._unidades_vendidas = 0

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, nome):
        self._titulo = nome
    
    @property
    def unidades_vendidas(self):
        return self._unidades_vendidas
    
    @unidades_vendidas.setter
    def unidades_vendidas(self, adiciona_unidade):
        self._unidades_vendidas += adiciona_unidade

class Fantasia(Livro):
    def __init__(self, titulo, ano, paginas, categoria_fantasia):
        super().__init__(titulo, ano, paginas)
        self.categoria_fantasia = categoria_fantasia


class Ficcao_cientifica(Livro):#Para definir que uma classe herda de outra define-se a superclasse entre parênteses
    def __init__(self, titulo, ano, paginas, categoria_ficcao_cientifica):
        super().__init__(titulo, ano, paginas) #Para reutilizar os atributos da classe Mãe usa-se o método super
        self.categoria_ficcao_cientifica = categoria_ficcao_cientifica

