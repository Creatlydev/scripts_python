from copy import deepcopy
from matrix_determinant import determinant



# c = "\u001b[38;5;221;m"
# print("{}2020".format(c))

def identidad(o):

    iden = []
    for i in range(o):
        iden.append([])
        for j in range(o):
            if i != j:
                v = 0
            else:
                v = 1
            iden[i].append(v)
    return iden


def rotar(m):
    rotada = []
    for i in range(len(m[0])):
        rotada.append([])

        for j in range(len(m)):
            rotada[i].append(m[j][len(m[0])-1 - i])

    return rotada


def inverse(m):

    det = determinant(m)
    if det == 0:
        return "No Es Posible Obtener La Inversa De La Matriz .. |m| = 0"

    copia = deepcopy(m)
    identida = identidad(len(m))

    for i in range(len(m)):
        copia[i] = copia[i] + identida[i]

    fila = 0
    column = 0

    for i in range(len(m)):

        if copia[fila][column] == 0:
            for k in range(fila+1, len(m)):
                if copia[k][column] != 0:
                    copia[fila], copia[k] = copia[k], copia[fila]

        pivote = copia[fila][column]

        for x in range(len(copia[0])):

            try:
                copia[fila][x] = round(copia[fila][x] / pivote, 8)
            except:
                pass

        for j in range(fila+1, len(m)):
            if copia[j][column] == 0:

                continue

            mul = copia[j][column]

            for n in range(column, len(copia[0])):

                res = copia[j][n] - (copia[fila][n] * mul)

                copia[j][n] = res

        fila += 1
        column += 1

    fila = -0
    column = -len(m)

    for i in range(len(m)):
        column -= 1
        fila -= 1

        for k in range(fila-1, -len(m)-1, -1):

            if copia[k][column] == 0:
                continue

            mul = copia[k][column]

            for x in range(-1, column-1, -1):

                res = copia[k][x] - (copia[fila][x] * mul)

                copia[k][x] = res

    for i in range(len(copia)):
        for j in range(len(copia[0])):
            num = copia[i][j]
            num_To_str = str(num)

            try:
                ind = num_To_str.index(".")
                decim = num_To_str[ind+1: ind+6]

            except ValueError:
                decim = None

            if num == 0.0 or decim == "0" or decim == "00000":
                copia[i][j] = int(num)

            else:

                copia[i][j] = float(round(num, 5))

    invertida = []
    for i in range(len(copia)):
        invertida.append(copia[i][len(m):])

    return "\n".join([str(i) for i in invertida])

