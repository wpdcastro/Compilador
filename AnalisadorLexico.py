from unicodedata import normalize

class AnalisadorLexico():

    reservados = [
                    "azia", 
                    "palpitacao", 
                    "Pressão Alta",
                    "falta de ar",
                    "fadiga" ,
                    "vomito",
                    "dor nas juntas",
                    "tosse",
                    "vermelidao"
    ]

    lista_sintomas = []

    simbolos_especiais = [",", ".","*",":","-","\"", "\'"] 

    def remover_acentos(self,txt):

        return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')   

    def realizar_analise(self, frase, linha) :

        frase = frase.split()

        array_tokenizado = []
    
        for token in frase:
            token_lower = token.lower() 
            token_lower = self.remover_acentos(token_lower)
            
            if token_lower in self.reservados:
                simbolo = "Sintoma"
                linha_tokenizado = [linha,token,simbolo]
            elif token_lower in self.simbolos_especiais:
                simbolo = "Simbolo Especial"
                linha_tokenizado = [linha,token,simbolo]
            else:
                simbolo = "Palavra fora do contexto"
                linha_tokenizado = [linha,token,simbolo]

            array_tokenizado.append(linha_tokenizado)
        
        return array_tokenizado

    def getSintomas(self, frase) :

        frase = frase.split()

        array_tokenizado = []
    
        for token in frase:
            
            token_lower = token.lower() 
            
            token_lower = self.remover_acentos(token_lower)
            
            if token_lower in self.reservados:
  
                linha_tokenizado = [token]

                array_tokenizado.append(linha_tokenizado)
        
        return array_tokenizado

