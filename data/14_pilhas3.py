"""
    Analizador de Expressões Mátematicas
"""

from lib.stack import Stack

simbolos = {
    "P": "parentese",
    "C": "colchete",
    "X": "chave"
}

expressao = "2 * 4 - { 7 / [5 - ( 7 * 9 ) + 1] * 3 } / 5"

analizador = Stack()       # Cria a pílha

def  verif_fechamento(tipo_fecha, pos_fecha, dados_fecha):
    print(f"DEBUG -> ")
    if dados_abre["tipo"] == tipo_fecha:
        print(f"Símbolo {tipo_fecha} aberto na posição {dados_abre['pos']} e fechado na posição {pos_fecha} ")
    else:
        print(f"ERRO: sìmbolo de fechamento do tipo {tipo_fecha} encontrado na posição {pos_fecha}; esperado símbolo do tipo {dados_abre['tipo']} ")

# Percorre a expressão em busca de parênteses, colchetes e chaves
for pos in range(len(expressao)):
    if expressao[pos] == "(":
        # Empilha informações sobre o abre parênteses
        analizador.push({ "tipo": "P", "pos": pos })
    elif expressao[pos] == "[":
        # Empilha informações sobre o abre colchetes
        analizador.push({ "tipo": "C", "pos": pos })
    elif expressao[pos] == "{": 
        # Empilha informações sobre o abre chaves
        analizador.push({ "tipo": "X", "pos": pos })

    elif expressao[pos] == ")": 
        analizador.push({ "P", analizador.pop() })

    elif expressao[pos] == "]": 
        analizador.push({ "C", analizador.pop() })
        
    elif expressao[pos] == "}": 
        analizador.push({ "X", analizador.pop() })

print(analizador.to_str())
    
