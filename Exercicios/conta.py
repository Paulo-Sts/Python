class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


conta_1 = Conta(55501, "Paulo", 700.0, 5000.0)
conta_2 = Conta(55502, "Eduardo", 300.0, 5000.0)

print(conta_1)
print(conta_2)