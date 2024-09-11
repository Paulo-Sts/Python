# São atributos definidos na classe e que pertencem a classe, independente do objeto
class Homem:
    especie = "Homo sapiens" # Atributos de classe podem ser acessados independetemente da existência de objetos do tipo da classe
    def __init__(self, nome, peso, cor):
        self.nome = nome
        self.peso = peso
        self.cor = cor
       

print(Homem.especie)