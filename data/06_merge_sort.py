# Algoritimo de ordenação merge sort
#
# No processo de ordenação, esse algoritimo de "desmonta" o vetor original
# contendo N elementos até obter N vetores de apenas um elementos cada um.
# Em seguida, usando a técnica de mesclagem (merge), "remonta" o vetor,
# dessa vez com os elementos já em ordem.

comps = 0
divisoes = 0
juncoes = 0

def merge_sort(lista):
    """
        Função que implementa o algoritimo merge sort usando o método recursivo
    """

    global comps, divisoes, juncoes

    print(f"Lista recebida: {lista}")

    # Só continua se a lista tiver mais de um elemento 
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2

    # Gera cópia da primeira metade da lista
    lista_esq = lista[:meio] # Do inicio ao meio - 1
    # Gera cópia da segunda metade da lista 
    lista_dir = lista[meio:] # Do meio ao fim 

    divisoes += 1

    # Chamamos recursivamente a função para continuar
    # repartindo a lista em metades
    lista_esq = merge_sort(lista_esq)
    lista_dir = merge_sort(lista_dir)

    print(f'>>> lista_esq: {lista_esq}')
    print(f'>>> lista_dir: {lista_dir}')
    # Junta as duas metades em uma única lista, ordenada
    pos_esq = 0
    pos_dir = 0
    ordenada = []   # Lista Vazia 

    while pos_esq < len(lista_esq) and pos_dir < len(lista_dir):
        # O elemento que se encontra na lista da direita
        # é menor que o que se encontra na lista da direita
        if lista_esq[pos_esq] < lista_dir[pos_dir]:
            ordenada.append(lista_esq[pos_esq])
            pos_esq += 1
        else:
            ordenada.append(lista_dir[pos_dir])
            pos_dir += 1
        comps += 1

    sobre = None    # A sobra da lista que ficou para trás

    if(pos_esq < pos_dir): # Houve sobra á esquerda
        sobra = lista_esq[pos_esq:] # Sobra do pos_esq até o final
    else:   # houve sobra à direita
        sobra = lista_dir[pos_dir:] # Sobra do pos_dir até o final 

    print(f'>>>> final ordenada: {ordenada  + sobra} ')

    # Retornamos a lista final ordenada, composta da ordenada + sobra
    juncoes += 1
    return ordenada + sobra     # "Soma" de duas listas

##################################################################

nums = [88, 44, 33, 0, 99, 55, 77, 22, 11, 66]

nums_ord = merge_sort(nums)

print(nums_ord)

##################################################################

from nomes_desord import nomes
from time import time
import tracemalloc

ini = time()
tracemalloc.start()

nomes_ord = merge_sort(nomes)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

print(nomes_ord)
print(f"Tempo: {fim - ini}")
print(f"Pico de mémoria: {mem_pico / 1024 / 1024}MB ")
print(f"Comparações: {comps}, Divisões {divisoes}, Junções {juncoes}  ")

tracemalloc.stop()
