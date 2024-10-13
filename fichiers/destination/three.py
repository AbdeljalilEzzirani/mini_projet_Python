# Challenge : Copie Sélective de Fichiers
# Objectif : Copier des fichiers spécifiques d'un répertoire à un autre.
# Travail à faire :
# Utilisez os.listdir() pour lister tous les fichiers dans un répertoire source.
# Utilisez shutil.copy() pour copier uniquement les fichiers avec une extension spécifique (par exemple, .csv) vers un répertoire de destination.

import os
import shutil

def copie_selective_fichiers(source_dir, destination_dir, extension='.csv'):
    files = os.listdir(source_dir)

    # Filter files that end with the specified extension
    # selected_files = [f for f in files if f.endswith(extension)]

    files = os.listdir(source_dir)
    text_files = []
    
    i = 0
    while i < len(files):  # Loop through the files
        if files[i].endswith('.py'):
            text_files.append(files[i])
        i += 1
    
    # combined_content = ""
    # Copy each selected file to the destination directory
    for file in files:
        src_path = os.path.join(source_dir, file)
        dst_path = os.path.join(destination_dir, file)
        
        shutil.copy(src_path, dst_path)
        print(f"File '{file}' has been copied to '{destination_dir}'")

# Example usage
source_dir = '/home/abdeljalil/Desktop/Mini_cahier/python/next-project/mini_projet_Python/fichiers'  # Replace with your source directory
destination_dir = '/home/abdeljalil/Desktop/Mini_cahier/python/next-project/mini_projet_Python/fichiers/destination'  # Replace with your destination directory

copie_selective_fichiers(source_dir, destination_dir, extension='.csv')
