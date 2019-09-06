#cadeia = input ("Dada uma gramatica, insira uma linha de comando:")
#frase = cadeia.split ()

cadeias = {
    "E": {
          "id": "TS", "num": "TS", "+": "", "-": "", "*": "", "/": "", "(": "E --> TS", ")": "", "$":""
         },
    "T": {
        "id": "T --> FG", "num": "T --> FG", "+": "", "-" : "", "*" : "","/": "", "(": "T --> FG", ")": "", "$": ""
         },
    "S": {
        "id": "S --> FG","num": "T --> FG", "+": "", "-": "", "*" : "","/": "","(": "T --> FG", ")": "", "$": ""
         },
    "G": {
        "id":"","num": "", "+": "G --> y", "-": "G --> y", "*" : "G --> *FG", "/" : "/FG", "(" : "", ")" : "G --> y", "$": "G --> y"
         },
    "F": {
        "id": "F --> id", "num": "F --> num", "+": "", "-": "", "*" : "","/": "", "(": "T --> (E)", ")": "", "$": ""
         }
}

cadeia = ["id", "+", "num", "*", "id"]
pilha  = ["E"]
regra  = ""

print("Pilha |      Cadeia                   | Regras   |")


ok = "false"

while (ok == "ok") :
    #pegar o topo da pilha
    topo_pilha = pilha[-1]
    topo_token = cadeia[-1]

    regra = cadeias[topo_pilha][topo_token]
    teste = "ok"
    print(pilha, "|" , cadeia, "|", topo_pilha + " --> " + regra)
    
    for caracter in regra:
        pilha.append(caracter)
        print(pilha)