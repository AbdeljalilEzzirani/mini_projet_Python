# 5. Melt et Pivot Tables (Reshaping des Données)
# Objectif : Utiliser melt() et pivot_table() pour remodeler les données en vue de l'analyse.
# Tâches :
# Transformer un DataFrame au format large en format long en utilisant melt() (par exemple, convertir un DataFrame de ventes par année en un format long avec "année" comme variable).
# Utiliser pivot_table() pour créer un tableau récapitulatif avec plusieurs fonctions d'agrégation (par exemple, pivot des ventes par région et année, en calculant à la fois la somme et la moyenne des ventes).
# Empiler et dés-empiler les niveaux d'un DataFrame multi-index pour remodeler les données.


import pandas as pd

# Creating a sample DataFrame
data = {
    'Region': ['North', 'South', 'East', 'West'],
    '2022_Sales': [15000, 20000, 17000, 18000],
    '2023_Sales': [16000, 21000, 18000, 19000],
    '2024_Sales': [17000, 22000, 19000, 20000]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)


def reshaping_donnees(df):
    # Melting the DataFrame
    df_melted = pd.melt(df, id_vars=['Region'], 
                        var_name='Year', value_name='Sales')

    # Extract year from 'Year' column
    df_melted['Year'] = df_melted['Year'].str.split('_').str[0]

    print("\nMelted DataFrame:\n", df_melted)

    # Creating a pivot table
    pivot_df = df_melted.pivot_table(index='Region', columns='Year', values='Sales', aggfunc=['sum', 'mean'])

    print("\nPivot Table:\n", pivot_df)

    # 4. Creating a Multi-Index DataFrame
    arrays = [['North', 'North', 'South', 'South', 'East', 'East', 'West', 'West'],
              ['2022', '2023', '2022', '2023', '2022', '2023', '2022', '2023']]
    index = pd.MultiIndex.from_arrays(arrays, names=('Region', 'Year'))
    sales_data = [15000, 16000, 20000, 21000, 17000, 18000, 18000, 19000]
    multi_index_df = pd.DataFrame(sales_data, index=index, columns=['Sales'])
    print("\nMulti-Index DataFrame:\n", multi_index_df)

    # 5. Stacking and Unstacking
    unstacked_df = multi_index_df.unstack(level='Year')
    print("\nUnstacked DataFrame:\n", unstacked_df)

    stacked_df = unstacked_df.stack(level='Year', future_stack=True)
    print("\nStacked DataFrame:\n", stacked_df)

reshaping_donnees(df)