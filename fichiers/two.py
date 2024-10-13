# Challenge : Recherche de Fichiers
# Objectif : Vérifier l'existence de fichiers spécifiques et les traiter.
# Travail à faire :
# Utilisez os.path.exists() pour vérifier si des fichiers de configuration (config.yaml) existent dans un répertoire donné.
# Si le fichier existe, ouvrez-le et affichez son contenu.


import os

def check_and_display_config(directory):
    file_path = os.path.join(directory, 'config.yaml')

    if os.path.exists(file_path):
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("File Content:\n", content)
    else:
        print(f"File '{file_path}' does not exist.")

directory = '/home/abdeljalil/Desktop/Mini_cahier/python/next-project/mini_projet_Python/fichiers'
check_and_display_config(directory)
