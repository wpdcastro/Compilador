#cadeia = input ("Dada uma gramatica, insira uma linha de comando:")
#frase = cadeia.split ()
from tabulate import tabulate

cadeias = {
    "E": {
            "id": ["T","S"], "num": ["T","S"], "+": []   , "-" : []   , "*":  [], "/": [], "(": ["T","S"], ")": [], "$":[]
         },
    "T": {
            "id": ["F","G"], "num": ["F","G"], "+": []   , "-" : []   , "*" : [], "/": [], "(": ["F","G"], ")": [], "$": []
         },
    "S": {
            "id": ["F","G"] ,"num": ["F","G"], "+": []   , "-" : []   , "*" : [], "/": "", "(": ["F","G"], ")": [], "$": []
         },
    "G": {
            "id": []        ,"num": []       , "+": ["y"], "-" : ["y"], "*" : ["*","F","G"], "/" : ["/","F","G"], "(" : [], ")" : ["y"], "$": ["y"]
         },
    "F": {
            "id": ["id"]    , "num": ["num"] , "+": []   , "-" : []   , "*" : [""],"/": [""], "(": ["(E)"], ")": [""], "$": [""]
         } 
}

cadeia = ["id", "+", "num", "*", "id"]
pilha  = ["E"]
regra  = ""
corpo = []

while (len(cadeia) > 0) :

    topo_pilha = pilha[-1]
    topo_token = cadeia[-1]

    if (topo_pilha == topo_token) :

        cadeia.pop(0)
        pilha.pop()
        regra = " - - -"

        corpo.append([pilha,cadeia,regra])

    else :
        
        regra = cadeias[topo_pilha][topo_token]

        if (len(regra) == 0) :
            regra = ["ERRO"]
            cadeia = []

        new_stack = pilha
        corpo.append([new_stack,cadeia,regra])

        pilha.pop()

        regra_aux = []

        for caracter in regra:
            regra_aux.insert(0,caracter)

        pilha = pilha + regra_aux


tabela = ["pilha" , "cadeia", "regra"]

print(tabulate(corpo,tabela,tablefmt="grid"))