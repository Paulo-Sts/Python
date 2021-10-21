#O property é uma forma de definir um método como propriedade do objeto, tornando seu acesso como se fosse igual ao acesso via atributo
class Pessoa:
    def __init__(self, nome, peso):
        self.__nome = nome
        self.__peso = peso

    @property
    def nome(self):
        return self.__nome

    @property
    def peso(self):
        return self.__peso

    @peso.setter #Para modificar o atributo usamos a referência do property que acessa ao valor do atributo e o modificamos via método setter
    def peso(self, peso):
        self.__peso = peso
