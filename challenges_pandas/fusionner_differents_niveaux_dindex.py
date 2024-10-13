# 8. Fusionner sur Différents Niveaux d'Index
# Objectif : Réaliser des fusions complexes en joignant sur différents niveaux d'un DataFrame à multi-index.
# Tâches :
# Créer deux DataFrames avec des index à plusieurs niveaux.
# Fusionner ces DataFrames en utilisant merge() ou join() sur un niveau spécifique de l'index.
# Expérimenter avec différents types de jointures (interne, externe, gauche, droite) et analyser l'impact sur les données.


import pandas as pd

# Création du premier DataFrame avec un multi-index (Region, Year)
arrays_1 = [
    ['North', 'North', 'South', 'South', 'East', 'East'],
    ['2022', '2023', '2022', '2023', '2022', '2023']
]
index_1 = pd.MultiIndex.from_arrays(arrays_1, names=('Region', 'Year'))

data_1 = {'Sales': [100, 150, 200, 250, 300, 350]}
df1 = pd.DataFrame(data_1, index_1)

# print("DataFrame 1:\n", df1)

# Création du deuxième DataFrame avec un multi-index (Region, Year)
arrays_2 = [
    ['North', 'North', 'South', 'West', 'East', 'East'],
    ['2022', '2023', '2022', '2023', '2022', '2023']
]
index_2 = pd.MultiIndex.from_arrays(arrays_2, names=('Region', 'Year'))

data_2 = {'Profit': [30, 50, 70, 90, 110, 130]}
df2 = pd.DataFrame(data_2, index_2)

# print("\nDataFrame 2:\n", df2)

def fusionner(df1, df2):
# Fusion des deux DataFrames en utilisant join sur le niveau 'Region'
    result = df1.join(df2, how='inner', lsuffix='_df1', rsuffix='_df2')

    print("\nRésultat de la jointure interne (inner join):\n", result)

#join outer
    result_outer = df1.join(df2, how='outer', lsuffix='_df1', rsuffix='_df2')

    print("\nRésultat de la jointure externe (outer join):\n", result_outer)

#join left
    result_left = df1.join(df2, how='left', lsuffix='_df1', rsuffix='_df2')

    print("\nRésultat de la jointure gauche (left join):\n", result_left)

#join right
    result_right = df1.join(df2, how='right', lsuffix='_df1', rsuffix='_df2')

    print("\nRésultat de la jointure droite (right join):\n", result_right)



fusionner(df1, df2)