from datetime import date, datetime

print(date.today()) # Método que retorna a data de hoje no formato AAAA/MM/DD

data_hoje = date.today()
data_como_texto = data_hoje.strftime("%d/%m/%Y") # Método que Converte para o padrão DD/MM/AAAA
print(data_como_texto)

data_e_horario_hoje = datetime.now() # O módulo datetime possui o método datetime que retorna data e hora ao mesmo tempo
data_e_horario_hoje_texto = data_e_horario_hoje.strftime("%d/%m/%Y %H:%M") # Podemos adicionar o parâmetro para horário com o mesmo método
print(data_e_horario_hoje_texto)