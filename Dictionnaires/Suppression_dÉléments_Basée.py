# Challenge : Suppression d'Éléments Basée sur une Condition
# Objectif : Supprimer les éléments d'un dictionnaire dont les valeurs respectent une condition.
# Travail à faire :
# Parcourez un dictionnaire avec items() et identifiez les éléments à supprimer.
# Supprimez ces éléments.
# Affichez le dictionnaire mis à jour.



import numpy as np

# Step 1: Create a NumPy array with temperature data
temperatures = np.array([22.5, 21.0, 23.5, 24.0, 20.0, 19.5, 25.0, 22.0, 24.5, 23.0])

# Step 2: Calculate the mean, median, and standard deviation
mean_temperature = np.mean(temperatures)
median_temperature = np.median(temperatures)
std_deviation = np.std(temperatures)

print (mean_temperature)
print (median_temperature)
print (std_deviation)