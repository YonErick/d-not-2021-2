"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""

# BUSCA BINÁRIA

# N = LISTA
# O = VALOR DE BUSCA
# P = INICIO
# Q = FIM
# R = MEIO

# ERRO = meio declarava meio = lista + valor de busca / 2, no lugar de  inicio + fim // (dividido) 2 

def m(n, o):
    p = 0       
    q = len(n) - 1    
    while p <= q:
        r = (p + q) // 2   
        if n[r] == o: 
            return r  
        elif o < n[r]: 
            q = r - 1  
        else: 
            p = r + 1  
    return -1

name = ["Erick", "Amanda", "Vanessa", "Jessica", "Caua"]
print(f"Posição da Vanessa:  {m (name,'Vanessa') }")
