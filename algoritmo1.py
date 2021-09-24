"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""

# QUICK SORT

# N = LISTA
# O = INICIO
# P = FIM
# Q = PIVOT
# R = DIV

# ERRO = O algoritmo não estava chamando as variaveis O e P na função

def m(n, o = 0, p = None):
    if p is None: 
        p = len(n) - 1

    if p <= o: 
        return

    q = p

    r = o - 1

    for i in range(o, p):

        if n[i] < n[q]:
            r += 1

            if r != i: n[r], n[i] = n[i], n[r]

    r += 1

    if n[q] < n[r] and q != r: 
        n[q], n[r] = n[r], n[q]

    m(n, o, r - 1)

    m(n, r + 1, p)

num = [1, 3, 5, 9, 2, 8]
m(num)
print(num)
