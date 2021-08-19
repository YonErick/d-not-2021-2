# Algoritimo de ordenação de Bubble sort
#
# Percorre a lista a ser ordenada em sucessivas passadas,
# trocando elementos adjacentes entre si quando o segundo for
# menor que o primeiro. Efetua tantas passadas quanto necessárias
# até que, na ultima passada, nenhuma troca seja efetuada.

comps = 0
passadas = 0
trocas = 0

def bubble_sort(lista):
    """
        Função que implementa o algoritimo de ordenação Bubble Sort
    """

    global comps, passadas, trocas
    comps = 0
    passadas = 0
    trocas = 0

    while True:  
        passadas += 1      #Loop Eterno
        trocou = False
        # Loop na lista até o PENULTIMO elemento: len(lista) - 2 
        # Ex. em uma lista de 10 elementos, len(lista) == 10
        # A ultima posição estará em len(lista) -1, ou seja 9
        # A penultima posição estará em len(lista) - 2, ou seja, 8
        for i in range(len(lista) - 1):
            comps += 1
            if lista[i + 1] < lista[i]:
                lista[i + 1], lista[i] = lista[i], lista[i + 1] # Faz a troca
                trocas += 1
                trocou = True

        # Se houve troca, a lista está ordenada e podemos interromper
        # o loop while
        if not trocou:  # Trocou == false
            break   # Interrompe o while 

#nums = [88, 44, 33, 0, 99, 55, 77, 22, 11, 66]

#Pior caso
#nums = [99, 88, 77, 66, 55, 44, 33, 22, 11, 0]

#Melhor caso
nums = [0, 11, 22, 33, 44, 55, 66, 77, 88, 99]

bubble_sort(nums)

print(nums)
print(f"Passadas: {passadas}, comparações: {comps}, trocas: {trocas}")

###############################################################################

from nomes_desord import nomes
from time import time

nomes_parcial = nomes[:20000] #Usa apenas os 20 mil primeiros nomes 

ini = time()
bubble_sort(nomes_parcial)
fim = time()

print(nomes_parcial)
print(f"Tempo: {fim - ini}")
print(f"Passadas: {passadas}, comparações: {comps}, trocas: {trocas}")
