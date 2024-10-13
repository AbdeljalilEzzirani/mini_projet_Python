# GroupBy avec Agrégation Personnalisée
# Objectif : Effectuer des agrégations complexes avec groupby() en utilisant des fonctions d'agrégation personnalisées.
# Tâches :
# Grouper les données par une ou plusieurs colonnes et appliquer une agrégation personnalisée (par exemple, calculer la moyenne pondérée).
# Utiliser agg() pour appliquer plusieurs fonctions d'agrégation (par exemple, somme, moyenne, écart-type) à différentes colonnes.
# Créer une fonction d'agrégation personnalisée qui applique plusieurs étapes (par exemple, normaliser puis agréger).

# import pandas as pd

# data = {
#     'category': ['Aniss', 'Aniss', 'Bouchra', 'Bouchra', 'Cotch', 'Cotch'],
#     'value1': [10, 20, 30, 40, 50, 60],
#     'value2': [5, 15, 25, 35, 45, 55]
# }

# def agregation(data):
#     data_frame = pd.DataFrame(data)
#     print ("\n < lister > : \n", data_frame)

#     grouped = data_frame.groupby("category").agg(total_v1 = ("value1", "sum"), total_v2 = ("value2", "mean"),
#     weighted_avg_v1=("value1", lambda x: (x * data_frame.loc[x.index, 'value2']).sum() / data_frame.loc[x.index, 'value2'].sum()),
#                                     std_v2=('value2', 'std'))
#     print("DataFrame après agrégation :\n", grouped)

#     normalized_grouped = data_frame.groupby('category').apply(lambda x: ((x['value1'] - x['value1'].mean()) /
#                                                                          x['value1'].std()).sum())
#     print ("\n < d'agrégation personnalisée qui applique plusieurs étapes > : \n", normalized_grouped)

# agregation(data)
