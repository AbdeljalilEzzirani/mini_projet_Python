# 1. Manipulation de Multi-Index
# Objectif : Travailler avec un DataFrame à multi-index et effectuer des opérations sur plusieurs niveaux.
# Tâches :
# Créer un DataFrame à multi-index à partir d'un jeu de données (par exemple : pays, ville, année comme index).
# Utiliser xs() pour extraire des sections transversales du DataFrame (par exemple, filtrer les données pour un pays spécifique).
# Inverser les niveaux de l'index (swaplevel()) et trier le DataFrame par niveaux d'index (sort_index()).
# Effectuer des opérations de groupement sur des niveaux spécifiques du multi-index.

import pandas as pd

#sample data
simple_data = {
    'population': [100000, 200000, 150000, 300000, 250000, 120000],
    'area': [100, 200, 150, 300, 250, 120]
}

#MultiIndex
index = pd.MultiIndex.from_tuples(
    [
        ('france', 'paris', 2020),
        ('france', 'lyon', 2020),
        ('germany', 'berlin', 2020),
        ('germany', 'munich', 2020),
        ('france', 'paris', 2021),
        ('germany', 'berlin', 2021)
    ],
    names=['country', 'city', 'year']
)

def multi_index(simple_data, index):
    data_frame = pd.DataFrame(simple_data, index=index)
    print ("< dataframe created with multi_index > : \n\n", data_frame)

    data_france = data_frame.xs("france", level="country")
    print ("\n < extraire des sections transversales du DataFrame pour france > : \n", data_france)

    swap_data = data_frame.swaplevel("city", "year")
    print ("\n < Inverser les niveaux de l'index > : \n", swap_data)

    sort_data = data_frame.sort_index(level="city")
    print ("\n < trier le DataFrame par niveaux d'index > : \n", sort_data)

    groupe = data_frame.groupby("country").sum()
    print ("\n < des opérations de groupement sur des niveaux spécifiques du multi-index > : \n", groupe)


multi_index(simple_data, index)