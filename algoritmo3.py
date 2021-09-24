"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""

# BUBBLE SORT

# N = LISTA
# O = TROCA
# P = I

# ERRO = O len estava chamando O = Troca, ao invez de chamar N = Lista

def m(n):
    while True:
        o = False
        for p in range(len(n) - 1):
            if n[p + 1] < n[p]:
                n[p + 1], n[p] = n[p], n[p + 1]
                o = True
        if not o:
            break

