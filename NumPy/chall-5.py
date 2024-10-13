# Challenge : Sélection Basée sur Conditions
# Objectif : Filtrer un tableau NumPy en fonction de conditions multiples.
# Travail à faire :
# Créez un tableau NumPy avec des valeurs numériques variées.
# Utilisez numpy.where() pour sélectionner les éléments supérieurs à un certain seuil.
# Créez un nouveau tableau avec les valeurs sélectionnées.

import numpy as np

# Create a NumPy array with numerical values
data = np.array([10, 25, 5, 60, 45, 30, 85, 15, 20])

# Define the threshold value for filtering
threshold = 30

# Step 2: Use numpy.where() to select elements greater than the threshold
# numpy.where(condition, value_if_true, value_if_false)
filtered_data = np.where(data > threshold, data, np.nan)  # Use NaN for values below the threshold

# Step 3: Create a new array with selected values (ignoring NaNs)
new_array = filtered_data[~np.isnan(filtered_data)] #  ~ == 'NOT'

# Output the results
print("Original Array:", data)
print("Filtered Array (Elements > 30):", new_array)
