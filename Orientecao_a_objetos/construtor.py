class Classe:

    def __init__(self): #O construtor é o responsável por inializar o objeto. 
        pass

#Exemplo

class Pessoa:

    def __init__(self, nome, data_nascimento, peso, sexo): #Por meio do init são definidos os atributos da classe
        self.nome = nome                                   #O self é a referência ao objeto criado
        self.data_nascimento = data_nascimento
        self.peso = peso
        self.sexo = sexo


pessoa1 = Pessoa("Eduardo", "02/04/1998", 67.15, "M")#A definição dos atributos do objeto são inicializados pela definição do objeto