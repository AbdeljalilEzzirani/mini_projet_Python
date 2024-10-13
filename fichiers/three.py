# Challenge : Copie Sélective de Fichiers
# Objectif : Copier des fichiers spécifiques d'un répertoire à un autre.
# Travail à faire :
# Utilisez os.listdir() pour lister tous les fichiers dans un répertoire source.
# Utilisez shutil.copy() pour copier uniquement les fichiers avec une extension spécifique (par exemple, .csv) vers un répertoire de destination.

import os
import shutil

def copie_selective_fichiers(source_dir, destination_dir, extension='.csv'):
    files = os.listdir(source_dir)
    selected_files = []
    i = 0
    while i < len(files):
        if files[i].endswith(extension):
            selected_files.append(files[i])
        i += 1

    for file in selected_files:
        src_path = os.path.join(source_dir, file)
        dst_path = os.path.join(destination_dir, file)
        
        shutil.copy(src_path, dst_path)
        print(f"File '{file}' has been copied to '{destination_dir}'")

source_dir = '/home/abdeljalil/Desktop/Mini_cahier/python/next-project/mini_projet_Python/fichiers'
destination_dir = '/home/abdeljalil/Desktop/Mini_cahier/python/next-project/mini_projet_Python/fichiers/destination'

copie_selective_fichiers(source_dir, destination_dir, extension='.csv')
