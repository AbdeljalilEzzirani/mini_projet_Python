# Challenge : Agrégation de Données

# Objectif : Agréger des données pour obtenir des statistiques par groupe.
# Travail à faire :
# Chargez un DataFrame contenant des informations sur les ventes.
# Utilisez pandas.DataFrame.groupby() pour calculer le total des ventes par région.
# Affichez les résultats.
# , 'North', 'East', 'South', 'West'        , 300, 400, 600, 900
import pandas as pd

data = {
    'region': ['north', 'south', 'east', 'west'],
    'sales': [500, 700, 200, 800]
}

def agregation_donnees(data):
    data_frame = pd.DataFrame(data)
    print ("data frame :\n", data_frame)


    data_frame_total = data_frame.groupby('region')['sales'].sum()
    print ("la calcule de total des ventes par région.", data_frame_total)


agregation_donnees(data)