# Challenge : Extraction et Traitement de Fichiers
# Objectif : Lire plusieurs fichiers texte et combiner leur contenu.
# Travail à faire :
# Utilisez os.listdir() pour lister tous les fichiers texte dans un répertoire.
# Utilisez open() pour lire chaque fichier et extraire son contenu.
# Combinez le contenu de tous les fichiers en un seul texte.

import os

def extract_and_combine_text_files(directory):
    files = os.listdir(directory)
    text_files = []
    
    i = 0
    while i < len(files):  # Loop through the files
        if files[i].endswith('.py'):
            text_files.append(files[i])
        i += 1
    
    combined_content = ""
    i = 0
    while i < len(text_files):  # Loop through the .py files
        file_path = os.path.join(directory, text_files[i])
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            combined_content += content + "\n"
        i += 1

    return combined_content

directory_path = '/home/abdeljalil/Desktop/Mini_cahier/python/next-project/mini_projet_Python/les_chaines'

combined_text = extract_and_combine_text_files(directory_path)
print("Combined Content:\n", combined_text)
