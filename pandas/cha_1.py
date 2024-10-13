# Challenge : Nettoyage de Données

# Objectif : Nettoyer un DataFrame en remplaçant les valeurs manquantes.
# Travail à faire :
# Chargez un DataFrame avec des données contenant des valeurs manquantes.
# Utilisez pandas.DataFrame.fillna() pour remplacer les valeurs manquantes par la moyenne des colonnes.
# Affichez le DataFrame nettoyé.

import pandas as pd
import numpy as np

data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [10, np.nan, 30, np.nan, 50]
}
def nettoyage_donnees(data):
    df = pd.DataFrame(data)

    print("original dataframe with missing values:")
    print(df)

                                                #Replace missing values with the mean of each column
    df_cleaned = df.fillna(df.mean())           #or switshthe missing values with

    print("\nCleaned DataFrame (missing values replaced by column mean):")
    print(df_cleaned)


nettoyage_donnees(data)
