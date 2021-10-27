class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome #Para usar os recursos de uma classe Mãe os atributos dela não podem ser privados
        self._idade = idade #Por convenção então adiciona-se apenas um underscore para informar que o atributo não seja acessado diretamente

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade

class Medico(Pessoa): #A classe Médico herda da classe Pessoa
    def __init__(self, nome, idade, hospital, departamento, crm):
        super().__init__(nome, idade)
        self.hospital = hospital
        self.departamento = departamento
        self.crm = crm

    @property
    def hospital(self):
        return self.hospital

class Advogado(Pessoa): #A classe Advogado herda da classe Pessoa
    def __init__(self, nome, idade, empresa, areaAtuacao, oab):
        super().__init__(nome, idade)
        self.empresa = empresa
        self.areaAtuacao = areaAtuacao
        self.oab = oab


minha_profissao = Medico("Paulo", 23, "Hospital Português", "Neurologia", 12345)
print("Minhas informações: {}".format(minha_profissao.nome))
print("Minhas informações: {}".format(minha_profissao.idade))
