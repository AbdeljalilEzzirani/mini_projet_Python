# Challenge : Création de Tableaux Croisés Dynamiques

# Objectif : Résumer les données avec un tableau croisé dynamique.
# Travail à faire :
# Chargez un DataFrame contenant des données de ventes par produit et par région.
# Utilisez pandas.DataFrame.pivot_table() pour créer un tableau croisé dynamique qui montre la somme des ventes par produit et par région.
# Affichez le tableau croisé dynamique.


import pandas as pd

# Sample data: sales data by product and region
data = {
    'product': ['A', 'B', 'A', 'B', 'A', 'C', 'B', 'C'],
    'region': ['North', 'North', 'South', 'South', 'East', 'East', 'West', 'West'],
    'sales': [200, 300, 150, 400, 250, 350, 450, 150]
}
def croises_dynamique(data):

    df = pd.DataFrame(data)

    pivot_table = df.pivot_table(values='sales', index='product', columns='region', aggfunc='sum', fill_value=0)

    print("Tableau Croisé Dynamique:\n", pivot_table)


croises_dynamique(data)