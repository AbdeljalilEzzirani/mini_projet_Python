# Challenge : Filtrage de Données
# Objectif : Filtrer un DataFrame pour ne conserver que les enregistrements répondant à une certaine condition.
# Travail à faire :
# Chargez un DataFrame avec des données financières.
# Filtrez le DataFrame pour ne conserver que les transactions
# d'un montant supérieur à 1000.
# Affichez le DataFrame filtré.

import pandas as pd


data = {
    'transaction_ID': [101, 102, 103, 104, 105],
    'client': ['ahmed', 'leo', 'saad', 'jack', 'maati'],
    'montante': [500, 1500, 750, 2000, 1200]
}


def filtrage_donnees(data):
    data_frame = pd.DataFrame(data)
    print ("\n --> data frame : \n", data_frame)

    data_frame_filtrage = data_frame[data_frame['montante'] > 1000]
    print ("\n --> data frame filtres : \n", data_frame_filtrage)



filtrage_donnees(data)