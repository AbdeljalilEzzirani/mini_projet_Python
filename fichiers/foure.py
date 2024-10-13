# Challenge : Création de Répertoires
# Objectif : Créer une structure de répertoires à partir d'une liste de noms.
# Travail à faire :
# Utilisez os.mkdir() pour créer un répertoire principal.
# Créez plusieurs sous-répertoires à l'intérieur du répertoire principal en utilisant une liste de noms.

import os

def creation_repertoires(main_directory, subdirectories):
    if not os.path.exists(main_directory):
        os.mkdir(main_directory)
        print(f"Main directory '{main_directory}' created.")
    else:
        print(f"Main directory '{main_directory}' already exists.")

    for subdirectory in subdirectories:
        subdirectory_path = os.path.join(main_directory, subdirectory)
        
        if not os.path.exists(subdirectory_path):
            os.mkdir(subdirectory_path)
            print(f"Subdirectory '{subdirectory}' created inside '{main_directory}'.")
        else:
            print(f"Subdirectory '{subdirectory}' already exists inside '{main_directory}'.")

main_directory = '/home/abdeljalil/Desktop/Mini_cahier/python/next-project/mini_projet_Python/fichiers/repertoire_principal'
subdirectories = ['subdir1', 'subdir2', 'subdir3']

creation_repertoires(main_directory, subdirectories)
