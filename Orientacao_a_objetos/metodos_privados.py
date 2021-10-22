#Métodos privados são métodos que não são acessados diretamente, sendo utilizados em outros métodos dentro da classe
class Carro:
    def __init__(self, modelo, velocidade, combustivel):
        self.modelo = modelo
        self.velocidade = velocidade
        self.combustivel = combustivel
        self.estado = False

    def __tem_combustivel(self):
       return self.combustivel > 0

    def liga(self):
        if(self.__tem_combustivel()):
            return print("Carro Ligado")
        else:
            return print("Carro sem combustível!")


meu_carro = Carro("Fox", 180.0, 0)
meu_carro.liga()

carro_2 = Carro("Gol", 180.0, 10)
carro_2.liga()