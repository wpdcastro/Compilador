#cadeia = input ("Dada uma gramatica, insira uma linha de comando:")
#frase = cadeia.split ()
from tabulate import tabulate
import copy

cadeias = {
    "E": { "id": ["T","S"], "num": ["T","S"], "+": [""], "-" : [""], "*":  [""], "/": [""], "(": ["T","S"], ")": [""], "$":[""]
         },
    "T": { "id": ["F","G"], "num": ["F","G"], "+": [""], "-" : [""], "*" : [""], "/": [""], "(": ["F","G"], ")": [""], "$": [""]
         },
    "S": { "id": [""] ,"num": [""], "+": ["+","T","S"], "-" : ["-", "T","S"]  , "*" : [""], "/": [""], "(": [""], ")": ["y"], "$": [""]
         },
    "G": { "id": [""],"num": [""], "+": ["y"], "-" : [""], "*" : ["*","F","G"] , "/" : ["/","F","G"] , "(" : [""], ")" : ["y"], "$": ["y"]
         },
    "F": { "id": ["id"],"num": ["num"]  , "+": [""], "-" : [""], "*" : [""], "/": [""], "(" : ["(", "E", ")"], ")": [""], "$": [""]
         } 
}

cadeia = ["id", "+", "id", "*", "id", "+", "(", "c", ")"]
pilha  = ["E"]
regra  = ""
corpo = []
add = 0
cont = 0

while (len(cadeia) > 0) :
 
    topo_pilha = pilha[-1]
    topo_cadeia = cadeia[0]
    if (len(cadeia) == 0) :
        print("RECONHECE")
        break
    
    if (topo_pilha == topo_cadeia) :
        
        cp_cadeia = copy.deepcopy(cadeia)
        cp_pilha = copy.deepcopy(pilha)

        cadeia.pop(0)
        pilha.pop()

        if (len(cadeia) == 0) :
            regra = " - - -"
            cp_cadeia2 = copy.deepcopy(cadeia)
            corpo.append([cp_pilha,cp_cadeia2,regra])

            regra = "Reconhece"
            corpo.append([cp_pilha,cp_cadeia2,regra])

        else :

            regra = " - - -"
            
        if (len(cadeia) > 0) :
            corpo.append([cp_pilha,cp_cadeia,regra])
        
    else :

        try : 
            regra = cadeias[topo_pilha][topo_cadeia]
        except:
            regra = ""

        if len(regra) == 0 :
            regra = "ERRO"
            
        
        cp_pilha = copy.deepcopy(pilha)
        cp_cadeia = copy.deepcopy(cadeia)
        corpo.append([cp_pilha,cp_cadeia,regra])

        if cont == 4 :
            print("corpo: ", corpo)
            
        pilha.pop()

        regra_aux = []

        if regra != "ERRO" :
            for caracter in regra:
                if caracter != "y" :
                    regra_aux.insert(0,caracter)

                
        cp_pilha = copy.deepcopy(pilha)

        pilha.extend(regra_aux)

        if regra == "ERRO" :
            break

    
    
tabela = ["pilha" , "cadeia", "regra"]
print(tabulate(corpo,tabela,tablefmt="grid"))

