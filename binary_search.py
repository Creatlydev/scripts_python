
def binary_search(
    lst: list,
    target: int
) -> tuple:
    """_summary_: Aplica el algoritmo de busqueda binaria para encontrar en numero dentro de una lista

    Args:
        lst (list): _description_ : Lista donde se buscara el elemento
        target (int): _description_ : Elemento a buscar dentro de la lista

    Returns:
        tuple: _description_ : Retornara el indice del elemento si existe, de lo contrario devuelve -1, adicionado para cualquiera de los dos casos el numero de comparaciones que se ha realizado
    """

    left = 0
    rigth = len(lst) - 1
    comparisons = 0

    while (left <= rigth):
        mid = (left + rigth) // 2
        comparisons += 1

        if (lst[mid] == target):
            return mid, comparisons
        elif (lst[mid] > target):
            rigth = mid - 1
        else:
            left = mid + 1

    # Si no se encontro el elemento retorna -1 como indice
    return -1, comparisons


def binary_search(
    lst: list,
    target: int,
    left: int,
    right: int
) -> int:
    if (left > right) :
        return -1
    
    mid = (left + right) // 2
    if (lst[mid] == target) :
        return mid
    elif (lst[mid] > target) :
        return binary_search(lst, target, left, mid - 1)
    else :
        return binary_search(lst, target, mid + 1, right)
