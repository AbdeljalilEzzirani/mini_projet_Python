# 3. Fonctions de Fenêtre (Window) et Rolling
# Objectif : Appliquer des calculs sur des fenêtres glissantes (rolling) et des fenêtres expansives sur des séries temporelles.
# Tâches :
# Calculer une moyenne mobile et une somme mobile pour une série temporelle donnée.
# Utiliser des fenêtres expansives pour calculer des statistiques cumulatives (par exemple, moyenne cumulative, somme cumulative).
# Appliquer une fonction personnalisée sur une fenêtre glissante (par exemple, corrélation glissante entre deux colonnes).

""""
# my code

import pandas as pd

data = {'values': [10, 20, 30, 40, 50, 60, 70, 80]}
data_frame = pd.DataFrame(data)

# Ajouter une deuxième colonne pour la corrélation
data_frame['values2'] = [15, 25, 35, 45, 55, 65, 75, 85]


def rolling(data_frame):
    print ("Moyenne Mobile et Somme Mobile in the < Rolling > \n")
    data_frame['moving_avg'] = data_frame['values'].rolling(window=3).mean()

    data_frame['moving_sum'] = data_frame['values'].rolling(window=3).sum()

    print(data_frame)

    print ("< Statistiques Cumulatives avec Fenêtres Expansives > : \n")
    data_frame['cumulative_mean'] = data_frame['values'].expanding().mean()

    data_frame['cumulative_sum'] = data_frame['values'].expanding().sum()

    print (data_frame)

    print ("< Appliquer une Fonction Personnalisée sur une Fenêtre Glissante > :\n")

    
    # Corrélation glissante entre les colonnes 'values' et 'values2' sur une fenêtre de 3
    data_frame['rolling_corr'] = data_frame['values'].rolling(window=3).corr(data_frame['values2'])
    
    print(data_frame)


rolling(data_frame)

"""


""" my code devloper """

import pandas as pd

# Création des données
data = {'values': [10, 20, 30, 40, 50, 60, 70, 80]}
data_frame = pd.DataFrame(data)

# Ajouter une deuxième colonne pour la corrélation
data_frame['values2'] = [15, 25, 35, 45, 55, 65, 75, 85]

# Fonction unique pour tous les calculs
def calculs_fenetre(data_frame):
    print("\n--- Calculs de Fenêtres Glissantes (Rolling) ---")
    
    # Moyenne mobile sur une fenêtre de 3
    data_frame['moving_avg'] = data_frame['values'].rolling(window=3).mean()

    # Somme mobile sur une fenêtre de 3
    data_frame['moving_sum'] = data_frame['values'].rolling(window=3).sum()

    print(data_frame[['values', 'moving_avg', 'moving_sum']])

    print("\n--- Statistiques Cumulatives avec Fenêtres Expansives ---")

    # Moyenne cumulative
    data_frame['cumulative_mean'] = data_frame['values'].expanding().mean()

    # Somme cumulative
    data_frame['cumulative_sum'] = data_frame['values'].expanding().sum()

    print(data_frame[['values', 'cumulative_mean', 'cumulative_sum']])

    print("\n--- Corrélation Glissante sur Fenêtre ---")

    # Corrélation glissante entre les colonnes 'values' et 'values2' sur une fenêtre de 3
    data_frame['rolling_corr'] = data_frame['values'].rolling(window=3).corr(data_frame['values2'])
    
    print(data_frame[['values', 'values2', 'rolling_corr']])

# Appel de la fonction pour effectuer tous les calculs
calculs_fenetre(data_frame)
