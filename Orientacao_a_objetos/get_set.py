#Por convenção em OO o acesso ao valor dos atributos ou modificações deles é feita por métodos getters e setters

class Aluno:

    def __init__(self, nome, matricula, media):
        self.__nome = nome
        self.__matricula = matricula
        self.__media = media

    def get_nome(self): #O get retorna o valor do atributo do objeto
        return self.__nome
    
    def get_matricula(self):
        return self.__matricula
    
    def get_media(self):
        return self.__media

    def set_media(self, media): #O set altera o valor do atributo
        self.__media = media


primeiro_aluno = Aluno("Paulo", "1234-5", 8.1)

print(primeiro_aluno.get_nome())
print(primeiro_aluno.get_matricula())
print(primeiro_aluno.get_media())
primeiro_aluno.set_media(8.5)
print(primeiro_aluno.get_media())
