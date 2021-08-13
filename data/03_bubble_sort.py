# Algoritimo de ordenação de Bubble sort
#
# Percorre a lista a ser ordenada em sucessivas passadas,
# trocando elementos adjacentes entre si quando o segundo for
# menor que o primeiro. Efetua tantas passadas quanto necessárias
# até que, na ultima passada, nenhuma troca seja efetuada.

def bubble_sort(lista):
    """
        Função que implementa o algoritimo de ordenação Bubble Sort
    """
    while True:        #Loop Eterno
        trocou = False
        # Loop na lista até o PENULTIMO elemento: len(lista) - 2 
        # Ex. em uma lista de 10 elementos, len(lista) == 10
        # A ultima posição estará em len(lista) -1, ou seja 9
        # A penultima posição estará em len(lista) - 2, ou seja, 8
        for i in range(len(lista) - 2):
            if lista[i + 1] < lista[i]:
                lista[i + 1], lista[i] = lista[i], lista[i + 1] # Faz a troca
                trocou = True

        # Se houve troca, a lista está ordenada e podemos interromper
        # o loop while
        if not trocou:  # Trocou == false
            break   # Interrompe o while 