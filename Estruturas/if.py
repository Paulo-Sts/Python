# O if é usado para executar um conjunto de comandos se uma condição booleana for verdadeira
print("1: Crédito", "2: Débito", "3: Dinheiro", sep="\n")
pagamento_usuario_str = input("Qual o método de Pagamento?\n")
pagamento_usuario = int(pagamento_usuario_str)

credito = pagamento_usuario == 1
debito = pagamento_usuario == 2
dinheiro = pagamento_usuario == 3

if(credito):
    print("Deseja parcelar?")
if(debito):
    print("Qual o cartão?")
if dinheiro: # O if aceita definir a condição sem o uso de parênteses
    print("O senhor(a) gostaria de troco?")