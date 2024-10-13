# Challenge : Écriture de Fichiers
# Objectif : Écrire du contenu dans un fichier texte.
# Travail à faire :
# Utilisez open() en mode écriture pour créer un nouveau fichier texte.
# Écrivez des lignes de texte dans le fichier en utilisant une boucle.
# Fermez le fichier et vérifiez que les données ont été correctement enregistrées.


def ecriture_fichier(nom_fichier, lignes):
    with open(nom_fichier, 'w') as fichier:
        i = 0
        while i < len(lignes):
            fichier.write(lignes[i] + '\n')
            i += 1

nom_fichier = 'output.txt'
lignes = ['bonjour monsieur coco cava', 'how is it going in your life ', 'the life is easy']

ecriture_fichier(nom_fichier, lignes)

print(f"Fichier '{nom_fichier}' a été créé avec succès.")
