liste_valeurs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def listecarres(liste_valeur):
    # liste_carres = list(map(lambda x: x * x, liste_valeurs))
    return (list(map(lambda x: x * x, liste_valeurs)))

print("\n  ->>> Liste d'origine :")
print(liste_valeurs)
print("\n  ->>> Liste des carrés :")
print(listecarres(liste_valeurs))
