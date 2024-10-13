# Challenge : Fusion de Données

# Objectif : Fusionner deux DataFrames sur une clé commune.
# Travail à faire :
# Chargez deux DataFrames : l'un contenant des informations sur les clients, l'autre sur les commandes.
# Fusionnez les DataFrames sur la colonne customer_id en utilisant pandas.DataFrame.merge().
# Affichez le DataFrame fusionné.

import pandas as pd

data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['abdo', 'wadie', 'saad', 'najib', 'noor'],
    'city': ['rabat', 'sale', 'casa', 'marakech', 'agadir']
}

orders_data = {
    'order_id': [101, 102, 103, 104, 105],
    'id': [1, 2, 2, 3, 4],
    'order_amount': [250, 150, 200, 300, 350]
}

def fusion_donnes(data, orders_data):
    df = pd.DataFrame(data)
    orders_df = pd.DataFrame(orders_data)
    fusionnez = pd.merge(df, orders_df, on='id', how='inner')
    print("Merged DataFrame:\n", fusionnez)


fusion_donnes(data, orders_data)



