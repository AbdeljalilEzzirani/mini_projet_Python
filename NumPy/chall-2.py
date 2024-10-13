# Challenge : Normalisation de Données
# Objectif : Normaliser un tableau de données pour qu'il ait une moyenne de 0 et un écart-type de 1.
# Travail à faire :
# Créez un tableau NumPy.
# Soustrayez la moyenne et divisez par l'écart-type pour normaliser les données.
# Affichez le tableau normalisé.

import numpy as np

data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

mean = np.mean(data)
std_dev = np.std(data)

normalized_data = (data - mean) / std_dev

print (mean)
print (std_dev)
print (normalized_data)

