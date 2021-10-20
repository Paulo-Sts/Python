#Podemos definir valores padrão para os atributos da classe e assim omiti-los ao criar um objeto

class Teclado:
    def __init__(self, marca, modelo, padrao = "ABNT2"):
        self.marca = marca
        self.modelo = modelo
        self.padrao = padrao

meu_teclado = Teclado("Logitech", "Bluetooth") #Atributo omitido, definindo o valor padrão
print(meu_teclado.padrao)

teclado_2 = Teclado("Microsoft", "Com cabo", "English") #Atributo especificado
print(teclado_2.padrao)