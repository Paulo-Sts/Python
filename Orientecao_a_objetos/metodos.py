#Os métodos são utilizados para acessar e manipular os atributos de um objeto que pertence a determinada classe, assim como realizar ações
class Carro:
    def __init__(self, modelo,velocidade, vel_max, combustivel,estado = False):
        self.modelo = modelo
        self.velocidade = velocidade
        self.vel_max = vel_max
        self.combustivel = combustivel
        self.estado = estado

    def liga(self): #Método Liga
        self.estado = True
        print("Carro ligado")
    
    def desliga(self): #Método desliga
        self.estado = False
        print("Carro desligado")
    
    def acelera(self, aceleracao): #Método acelera
        if(self.estado == False):
            print("Carro desligado")
        elif(aceleracao > self.vel_max):
            print("Velocidade: {}".format(self.vel_max))
        else:
            self.velocidade += aceleracao
            print("Velocidade: {}".format(self.velocidade))
    
    def abastece(self, quantidade): #Método abastece
        self.combustivel += quantidade
        if(self.combustivel > 60):
            print("Tanque 60 litros")
        else:
            print("Tanque {} litros".format(self.combustivel))

#Criando objeto e testando
meu_carro = Carro("Fox",0, 180, 20)
meu_carro.liga()
meu_carro.acelera(50)
meu_carro.desliga()
meu_carro.acelera(60)
meu_carro.abastece(50)
