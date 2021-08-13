# Algoritimo de Busca Binária
#
# Dada uma lista, que deve estar PREVIAMENTE ORDENADA, e um valor de
# busca, divide a lista em duas metades e procura pelo valor de busca
# apenas na metade onde o valor poderia estar. Novas subdivisões são
# feitas até que se encontre o valor de busca ou que reste apenas uma
# sublista vazia, quando se conclui que o valor de busca não existe na 
# lista.
from time import time
from lista_nomes import nomes

comps = 0 # Declarando uma variável global

def busca_binaria(lista, valor_busca):
    """
        Função que implementa o algoritmo de busca binária

        Retorna a posição onde valor_busca foi encontrado ou o valor convencional -1 se valor_busca não existir na lista
    """
    global comps # Indica que estamos usando a variável declarada na linha 13
    comps = 0

    ini = 0              # Primeira posição
    fim = len(lista) -1  # Ultima Posição

    while ini <= fim:
        meio = (ini + fim) // 2    # Operador // é divisão inteira

        # Caso 1: lista[meio] é igual a valor_busca
        if lista[meio] == valor_busca: # ENCONTROU!
            comps += 1
            return meio                # Meio é a posição onde valor_busca está na lista
        
        # Caso 2: valor_busca é menor que lista[meio]
        elif valor_busca < lista[meio]:
            comps += 2
            fim = meio -1   # Descarta a 2 metade da lista
        
        # Caso 3: valor_busca é maior que lista[meio]~
        else:
            comps += 2
            ini = meio + 1 # Descarta a 1 metade da lista

    # Caso 4: valor_busca não encontrado na lista
    return -1

comps = 0
hora_ini = time()
print(f"Posição de ERICK: {busca_binaria(nomes, 'ERICK')}")
hora_fim = time()
print(f"Tempo gasto procurando ERICK: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de ZULEICA: {busca_binaria(nomes, 'ZULEICA')}")
hora_fim = time()
print(f"Tempo gasto procurando ZULEICA: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de ORKUTILSON: {busca_binaria(nomes, 'ORKUTILSON')}")
hora_fim = time()
print(f"Tempo gasto procurando ORKUTILSON: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de BELERINA: {busca_binaria(nomes, 'BELERINA')}")
hora_fim = time()
print(f"Tempo gasto procurando BELERINA: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de LUNISVALDO: {busca_binaria(nomes, 'LUNISVALDO')}")
hora_fim = time()
print(f"Tempo gasto procurando LUNISVALDO: {(hora_fim - hora_ini) * 1000}ms")

print(f"Nome exatamente no meio da lista: {nomes[len(nomes) // 2]} ")

hora_ini = time()
print(f"Posição de JERDERSON: {busca_binaria(nomes, 'JERDERSON')}, {comps} comparações ")
hora_fim = time()
print(f"Tempo gasto procurando JERDERSON: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de AARAO: {busca_binaria(nomes, 'AARAO')}, {comps} comparações ")
hora_fim = time()
print(f"Tempo gasto procurando AARAO: {(hora_fim - hora_ini) * 1000}ms")