# Barbara Carline -
# Bruno Henrique  - 
# William Castro  - 571644

# Arquivo que executa as classes disponiveis do compilador python

# Importando analisadores
from AnalisadorLexico import AnalisadorLexico
from tabulate import tabulate
import json

# Realizando etapa de analise lexica
lexico = AnalisadorLexico()

frases = ["Azia, quando tomo café Palpitação", "Tenho Palpitação", "TENHO TOSSE", "Palpitação","palpitacao"]

linha = 0
teste = []
sintomas = []
for frase in frases : 
	result = lexico.realizar_analise(frase, linha)
	sintomas.append(lexico.getSintomas(frase))
	
	teste = teste + result
	linha = linha + 1

#print(teste)
tabela = ["linha" , "token", "simbolo"]
print(tabulate(teste,tabela,tablefmt="grid"))


print(json.dumps(sintomas))