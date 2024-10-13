# Challenge : Opérations Matricielles
# Objectif : Effectuer des opérations sur des matrices en utilisant NumPy.
# Travail à faire :
# Créez deux matrices NumPy.
# Effectuez une multiplication matricielle.
# Calculez la transposée et l'inverse de la matrice résultante.

import numpy as np

matrix1 = np.array([[1, 2, 3], [4, 5, 6]])

matrix2 = np.array([[7, 8], [9, 10], [11, 12]])

def operation_matrix(matrix1, matrix2):

    result_matrix = np.matmul(matrix1, matrix2)

    transpose_matrix = np.transpose(result_matrix)

    if result_matrix.shape[0] == result_matrix.shape[1]:
        inverse_matrix = np.linalg.inv(result_matrix)
    else:
        inverse_matrix = None
    return transpose_matrix, inverse_matrix

result_transpose, result_inverse = operation_matrix(matrix1, matrix2)

print ("\n", result_transpose)
print ("\n", result_inverse)
