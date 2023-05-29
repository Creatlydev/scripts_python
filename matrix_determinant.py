'''   Determinante de matrices   '''
from copy import deepcopy


def mul_diag(matriz) :
    mul= 1
    for i in range(len(matriz)) :
        mul *= matriz[i][i]
    return mul


def is_triangular_matrix(matriz) :
    
    for i in range(len(matriz)) :
        for j in range(len(matriz)) :
            if (i > j) :
                if (matriz[i][j]) != 0 :
                    return False
    return True

def determinant(matriz) :
    
    # Comprueba si alguna fila de la matriz es nula
    for i in range(len(matriz)) :
        if (0 in matriz[i]) :
            if (matriz[i].count(0) == len(matriz[i])) :
                return 0
    
    # Comprueba si alguna columna de la matriz es nula 
    cont= 0
    for i in range(len(matriz)) :
        for j in range(len(matriz)) :
            if (matriz[j][i] == 0) :
                cont += 1
        if (cont == len(matriz)) :
            return 0
        else :
            cont= 0
    
    # Dado que no hay ninguna fila ni columna nula se hace una copia de la matriz para operar
    matrix_copy= deepcopy(matriz)
    column= 0
    sign= 1
    
    for i in range(1, len(matrix_copy)) :
        if (is_triangular_matrix(matrix_copy)) :
            return sign * round(mul_diag(matrix_copy), 5)
        
        if (matrix_copy[i-1][i-1] == 0) :
            for k in range(i, len(matrix_copy)) :
                if (matrix_copy[k][i-1] != 0) :
                    matrix_copy[i - 1], matrix_copy[k]= matrix_copy[k], matrix_copy[i - 1]
                    sign *= -1
        
        for j in range(i, len(matrix_copy)) :
            if (matrix_copy[j][column] == 0) :
                continue
            
            div= round(matrix_copy[j][column] / matrix_copy[column][column], 8)
            
            for k in range(column, len(matrix_copy)) :
                res= round(
                    matrix_copy[j][k] - (matrix_copy[column][k] * div),
                    5
                    )
        column += 1
    
    return sign * round(mul_diag(matriz), 5) 