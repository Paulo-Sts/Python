# Podemos criar, manipular e ler arquivos por meio de funcionalidades do python

arquivo1 = open("Arquivos/nomes.txt", "w") # A função open() abre um arquivo ou cria um se não existir
                                          # Ela recebe o parâmetro do nome do arquivo e o tipo de maninulação (escrita/leitura)
arquivo1.write("Paulo\n") # A função write escreve no arquivo

arquivo1.close() # Após acessar um arquivo é necessário fecha-lo, isso é feito com a função close()

arquivo1 = open("Arquivos/nomes.txt", "r") # No modo de leitura podemos ler todo o arquivo com a função read(), ou ler linha por linha com a função readline()
print(arquivo1.readline().strip())

arquivo1.close()

arquivo1 = open("Arquivos/nomes.txt", "a") # A opção a(append) adiciona conteúdo ao arquivo sem apagar o que já existe
arquivo1.write("Cleide\n")

arquivo1.close()

# Leitura de todo o arquivo
arquivo1 = open("Arquivos/nomes.txt", "r")
print(arquivo1.read().strip())

arquivo1.close()
