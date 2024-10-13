# 6. Méthode Apply et Fonctions Vectorisées
# Objectif : Utiliser apply(), applymap(), et pipe() pour appliquer des fonctions personnalisées efficacement sur des lignes et colonnes.
# Tâches :
# Écrire une fonction personnalisée et l'appliquer ligne par ligne ou colonne par colonne avec apply() (par exemple, calculer un score pondéré pour chaque ligne).
# Appliquer une fonction élément par élément avec applymap() (par exemple, convertir des valeurs de température entre Celsius et Fahrenheit).
# Enchaîner plusieurs opérations avec pipe() pour un code plus propre.

import pandas as pd

#dataframes simple for students
data_students = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David'],
    'Math': [85, 78, 92, 88],
    'Science': [90, 82, 95, 87],
    'English': [88, 75, 85, 93]
}
df_students = pd.DataFrame(data_students)

#dataframe temperatures in celsius
data_temperatures = {
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Jan': [-2, 15, -5],
    'Feb': [0, 16, -3],
    'Mar': [5, 18, 4]
}
df_temperatures = pd.DataFrame(data_temperatures)

#dataframe sales in the years
data_sales = {
    'Product': ['A', 'B', 'C', 'D'],
    'Sales_2022': [1000, 1500, 2000, 1200],
    'Sales_2023': [1100, 1600, 2100, 1300]
}
df_sales = pd.DataFrame(data_sales)



def combined_operations(df_students, df_temperatures, df_sales):
#1 -_- apply mrthode apply() for calculate a weighted score for chaque student
    def weighted_score(row):
        return 0.3 * row['Math'] + 0.4 * row['Science'] + 0.3 * row['English']

    df_students['Weighted_Score'] = df_students.apply(weighted_score, axis=1)
            # axis=1: This tells apply() to operate on rows (because axis=1 refers to rows, while axis=0 would refer to columns).
    
                                    # celsius_columns = df_temperatures.columns[1:]  #skip the 'City' column
                                    # df_temperatures[celsius_columns] = (df_temperatures[celsius_columns] * 9/5) + 32

# #2 -_- converter Celsius to Fahrenheit without applymap()
    #define or applique la formule 
    def celsius_to_fahrenheit(celsius_value):
        return celsius_value * 9/5 + 32

    # Step 2: Apply the function to the temperature columns using applymap()
    celsius_columns = df_temperatures.columns[1:]#skip the 'City' column
    df_temperatures[celsius_columns] = df_temperatures[celsius_columns].apply(celsius_to_fahrenheit)


#3 -_- using pipe() to chain operations on the sales data
    def calculate_growth(df): #nisebaat nomoow lkoool product in one years
        df['Growth'] = df['Sales_2023'] / df['Sales_2022'] - 1
        return df

    def label_performance(df): #just un commentaire for performance in the chaque product
        df['Performance'] = df['Growth'].apply(lambda x: 'Good' if x > 0.05 else 'Needs Improvement')
        return df

    df_sales = df_sales.pipe(calculate_growth).pipe(label_performance)

    # Returning the modified DataFrames
    return df_students, df_temperatures, df_sales


#finish call function
df_students, df_temperatures, df_sales = combined_operations(df_students, df_temperatures, df_sales)

#finnalemment display resulting dataframes
print("\nUpdated Students DataFrame with Weighted Scores:\n", df_students)
print("\nUpdated Temperatures DataFrame (Fahrenheit):\n", df_temperatures)
print("\nUpdated Sales DataFrame with Growth and Performance:\n", df_sales)























# import pandas as pd

# def combined_operations(df_students, df_temperatures, df_sales):
#     # 1. Calculate weighted score for students using apply (row-wise)
#     def weighted_score(row):
#         return 0.3 * row['Math'] + 0.4 * row['Science'] + 0.3 * row['English']

#     df_students['Weighted_Score'] = df_students.apply(weighted_score, axis=1)

#     # 2. Convert Celsius to Fahrenheit without applymap (clearer loop)
#     def celsius_to_fahrenheit(celsius):
#         return (celsius * 9/5) + 32

#     for col in df_temperatures.columns[1:]:
#         df_temperatures[col] = df_temperatures[col].apply(celsius_to_fahrenheit)

#     # 3. Calculate growth and label performance for sales data
#     df_sales['Growth'] = (df_sales['Sales_2023'] - df_sales['Sales_2022']) / df_sales['Sales_2022']
#     df_sales['Performance'] = df_sales['Growth'].apply(lambda x: 'Good' if x > 0.05 else 'Needs Improvement')

#     # Return the modified DataFrames
#     return df_students, df_temperatures, df_sales

# # Sample DataFrames (same as before)
# data_students = {
#     'Student': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Math': [85, 78, 92, 88],
#     'Science': [90, 82, 95, 87],
#     'English': [88, 75, 85, 93]
# }
# df_students = pd.DataFrame(data_students)

# data_temperatures = {
#     'City': ['New York', 'Los Angeles', 'Chicago'],
#     'Jan': [-2, 15, -5],
#     'Feb': [0, 16, -3],
#     'Mar': [5, 18, 4]
# }
# df_temperatures = pd.DataFrame(data_temperatures)

# data_sales = {
#     'Product': ['A', 'B', 'C', 'D'],
#     'Sales_2022': [1000, 1500, 2000, 1200],
#     'Sales_2023': [1100, 1600, 2100, 1300]
# }
# df_sales = pd.DataFrame(data_sales)

# # Call the function
# df_students, df_temperatures, df_sales = combined_operations(df_students, df_temperatures, df_sales)

# # Show results
# print("\nUpdated Students DataFrame:\n", df_students)
# print("\nUpdated Temperatures DataFrame (Fahrenheit):\n", df_temperatures)
# print("\nUpdated Sales DataFrame with Growth and Performance:\n", df_sales)

