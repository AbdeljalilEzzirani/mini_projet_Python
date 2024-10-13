# Challenge : Comparaison de Tableaux
# Objectif : Comparer deux tableaux NumPy et trouver les éléments qui diffèrent.
# Travail à faire :
# Créez deux tableaux NumPy similaires avec de petites différences.
# Utilisez numpy.where() pour trouver les indices où les éléments diffèrent.
# Affichez les indices et les valeurs correspondantes des deux tableaux.

import numpy as np

data0 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
data1 = np.array([10, 200, 30, 400, 50, 600, 70, 800, 90, 1000])

def comparaison_tab(data0, data1):
    indices = np.where(data0 != data1)

    # i = 0
    # while i < len(indices):
    for index in indices:
        # index = indices[i]
        print(f"Index {index}: \nArray1 = {data0[index]}, \nArray2 = {data1[index]}")
        print(f"Index  {index}")
        print(f"array0 {data0[index]}")
        print(f"array1 {data1[index]}")
        # i += 1

comparaison_tab(data0, data1)