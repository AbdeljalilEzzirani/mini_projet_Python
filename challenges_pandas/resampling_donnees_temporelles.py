# 4. Resampling des Données Temporelles
# Objectif : Rééchantillonner des données temporelles à différentes fréquences et appliquer des fonctions d'agrégation.
# Tâches :
# Rééchantillonner des données journalières à des intervalles hebdomadaires, mensuels, et annuels, puis calculer des statistiques d'agrégation pour chaque période.
# Utiliser resample() pour remplir les données manquantes avec des méthodes forward-fill et backward-fill.
# Rééchantillonner des données temporelles irrégulières et interpoler les valeurs manquantes avec différentes méthodes.

import pandas as pd
import numpy as np

""" Création d'un DataFrame avec des données temporelles journalières """

date_range = pd.date_range(start='2023-01-01', end='2023-01-15', freq='D')

data = {
    'date': date_range,
    'value': np.random.randint(1, 100, size=len(date_range))
}

df = pd.DataFrame(data)

#print ("this pour Rééchantillonnage de données temporelles irrégulières : \n")

irregular_dates = pd.to_datetime(['2023-01-01', '2023-01-03', '2023-01-07', '2023-01-10', '2023-01-12'])
irregular_data = {
    'date': irregular_dates,
    'value': [10, 20, 30, 40, 50]
}

irregular_df = pd.DataFrame(irregular_data)

def resampling_tempoorelles(df):
    df.set_index('date', inplace=True)

    print("Données originales :\n", df)

    print ("Rééchantillonnage à des intervalles hebdomadaires, mensuels, et annuels")

    weekly_resampled = df.resample('W').mean()
    print("\nMoyenne hebdomadaire :\n", weekly_resampled)

    monthly_resampled = df.resample('ME').mean()
    print("\nMoyenne mensuelle :\n", monthly_resampled)

    annual_resampled = df.resample('YE').mean()
    print("\nMoyenne annuelle :\n", annual_resampled)


    print ("Remplissage des données manquantes avec forward-fill et backward-fill :  \n")
    print ("Ajouter des dates manquantes pour démontrer le remplissage  :\n")

    df = df.reindex(pd.date_range(start='2023-01-01', end='2023-01-20', freq='D'))
    print("\nDonnées après réindexation (avec valeurs manquantes) :\n", df)

    print ("Remplissage des valeurs manquantes : \n")

    df_ffill = df.ffill()  # Forward fill
    df_bfill = df.bfill()  # Backward fill

    print("\nDonnées avec forward-fill :\n", df_ffill)
    print("\nDonnées avec backward-fill :\n", df_bfill)

    #******************

    print ("Création d'un DataFrame avec des dates irrégulières : \n")
    irregular_df.set_index('date', inplace=True)

    # Rééchantillonnage et interpolation
    irregular_resampled = irregular_df.resample('D').mean()  # Rééchantillonnage quotidien
    interpolated = irregular_resampled.interpolate(method='linear')  # Interpolation linéaire

    print("\nDonnées rééchantillonnées (irrégulières) avec interpolation :\n", interpolated)


resampling_tempoorelles(df)






# import pandas as pd
# import numpy as np

# # Création d'un DataFrame avec des données temporelles journalières
# date_range = pd.date_range(start='2023-01-01', end='2023-01-15', freq='D')

# data = {
#     'date': date_range,
#     'value': np.random.randint(1, 100, size=len(date_range))
# }

# df = pd.DataFrame(data)

# # Création d'un DataFrame avec des dates irrégulières
# irregular_dates = pd.to_datetime(['2023-01-01', '2023-01-03', '2023-01-07', '2023-01-10', '2023-01-12'])
# irregular_data = {
#     'date': irregular_dates,
#     'value': [10, 20, 30, 40, 50]
# }
# irregular_df = pd.DataFrame(irregular_data)

# def resampling_temporales(df, irregular_df):
#     # Set the index for the main DataFrame
#     df.set_index('date', inplace=True)

#     print("Données originales :\n", df)

#     print("Rééchantillonnage à des intervalles hebdomadaires, mensuels, et annuels")

#     weekly_resampled = df.resample('W').mean()
#     print("\nMoyenne hebdomadaire :\n", weekly_resampled)

#     monthly_resampled = df.resample('ME').mean()  # Use 'ME' if needed
#     print("\nMoyenne mensuelle :\n", monthly_resampled)

#     annual_resampled = df.resample('YE').mean()  # Use 'YE' if needed
#     print("\nMoyenne annuelle :\n", annual_resampled)

#     print("Remplissage des données manquantes avec forward-fill et backward-fill :\n")
#     print("Ajouter des dates manquantes pour démontrer le remplissage :\n")

#     # Reindexing the DataFrame to include missing dates
#     df = df.reindex(pd.date_range(start='2023-01-01', end='2023-01-20', freq='D'))
#     print("\nDonnées après réindexation (avec valeurs manquantes) :\n", df)

#     print("Remplissage des valeurs manquantes :\n")

#     # Forward fill and backward fill
#     df_ffill = df.ffill()  # Forward fill
#     df_bfill = df.bfill()  # Backward fill

#     print("\nDonnées avec forward-fill :\n", df_ffill)
#     print("\nDonnées avec backward-fill :\n", df_bfill)

#     # Rééchantillonnage et interpolation pour les données irrégulières
#     irregular_df.set_index('date', inplace=True)
#     irregular_resampled = irregular_df.resample('D').mean()  # Rééchantillonnage quotidien
#     interpolated = irregular_resampled.interpolate(method='linear')  # Interpolation linéaire

#     print("\nDonnées rééchantillonnées (irrégulières) avec interpolation :\n", interpolated)

# # Call the function with both DataFrames
# resampling_temporales(df, irregular_df)
