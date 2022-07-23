import dados_pessoais
import dados_profissionais
# Podemos importar arquivos e funcionalidades de outros arquivos tornando o código modularizado
# Ao importar um arquivo ele é executado automaticamente, mas se ele tiver funções elas só são executadas quando chamadas
# Para executar uma função de um módulo usamos a propriedade .(ponto) dessa forma (nome_modulo.nome_funcionalidade())
print("Meu nome é {}".format(dados_pessoais.nome()))
print("Meu segundo nome é {}".format(dados_pessoais.segundo_nome()))
print("Meu sobrenome é {}".format(dados_pessoais.sobrenome()))
print("Meu nome completo é {} {} {} e eu tenho {} anos.".format(dados_pessoais.nome(), dados_pessoais.segundo_nome(),dados_pessoais.sobrenome(), dados_pessoais.idade()))

print("Minha profissão é {}".format(dados_profissionais.profissao()))