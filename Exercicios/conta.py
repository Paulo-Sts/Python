class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Seu saldo é {}".format(self.__saldo))

    def deposito(self, valor):
        self.__saldo += valor
    
    def __pode_sacar(self, valor): #Métodos privados, são métodos que são usados por outros métodos e não são acessados diretamente
        limite = self.__saldo + self.__limite
        return valor <= limite

    def saque(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} é maior que o disponível!".format(valor))
    
    def transferencia(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__titular

    @limite.setter
    def limite(self, limite):
        self.__limite = limite    
    
    @staticmethod #Métodos estáticos são métodos pertencentes a classe independentes dos objetos
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}

conta_1 = Conta(55501, "Paulo", 700.0, 5000.0)
conta_2 = Conta(55502, "Eduardo", 300.0, 5000.0)

print(conta_1.extrato())
print(conta_2.extrato())

conta_1.transferencia(50.0,conta_2)
print(conta_1.extrato())
print(conta_2.extrato())

conta_1.saque(10000.0)

print(Conta.codigo_banco())
print(Conta.codigos_bancos())