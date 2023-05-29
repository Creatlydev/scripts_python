''' Determinante de matrices con metodo de Adjuntas '''

def adjoint(
    matriz: list,
    row: int,
    column: int
) -> list:

    return [
        [
            matriz[i][j] for j in range(len(matriz[0])) if j != column
        ]
        for i in range(len(matriz)) if i != row
    ]


def determinant(
    matriz: list
) -> int:
    """_summary_ : Calculara la determinante de una matriz dada

    Args:
        matriz (list): _description_ : matriz a calcular

    Returns:
        int: _description_ : determinante calculado de la matriz
    """

    if (len(matriz) == 2):
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    row = 0
    det = 0

    for column in range(len(matriz[0])):
        adjt = adjoint(matriz, row, column)
        det += pow(-1, (column + row)) * \
            matriz[row][column] * determinant(adjt)

    return det