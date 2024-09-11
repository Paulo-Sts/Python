class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def formata_data(self):
        print("{}".format(self.dia),"{}".format(self.mes),"{}".format(self.ano), sep="/")


d = Data(20,10,2021)

d.formata_data()