def partition(lista, low, high):
    """
    Partición de la lista original.
    Aquí se produce la comparación y cambio de valores, usando como referencia el pivote.
    """
    i = low - 1  #Índice de elemento más pequeño
    pivote = lista[high]  #Pivote

    for j in range(low, high):
        if lista[j] <= pivote:  #Comprobación de valores con el pivote
            i = i + 1
            lista[i], lista[j] = lista[j], lista[i]     #Cambio de valores

    lista[i + 1], lista[high] = lista[high], lista[i + 1]     #Cambio de valores
    return i + 1

def quick_sort(items, low, high):
    """
    Quick sort ordena cualquier lista de números más rápido que cualquir otro algoritmo.
    Se basa en la partición de la lista en más pequeñas, las cuales se comparan con el punto de pivote y se modifica.
    Este algoritmo, entra en la categoría del enfoque 'Divide y vencerás'
    """

    if low < high:
        pivote_indice = partition(items, low, high);

        quick_sort(items, low, pivote_indice-1)     #Antes de la partición
        quick_sort(items, pivote_indice+1, high)     #Después de la partición

    return