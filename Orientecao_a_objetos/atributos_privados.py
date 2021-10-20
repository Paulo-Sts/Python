#Em python não todos os atributos são públicos, mas para informar que eles não devem ser acessados diretamente usa-se dois __(underscore) na definição do atributo.
class Celular:
    def __init__(self, marca, modelo, estado):
        self.__marca = marca
        self.__modelo = modelo
        self.__estado = estado
    
    def liga(self):
        self.__estado = True
        print("Celular ligado")
    
    def desliga(self):
        self.__estado = False
        print("Celular desligado")


meu_celular = Celular("Motorola", "Moto G8 Pro", False)

#Usando encapsulamento 
meu_celular.liga() #A manipulação do estado do objeto é feita por meio dos métodos de sua classe
meu_celular.desliga()