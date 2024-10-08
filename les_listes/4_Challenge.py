liste_a = [1, 2, 3, 4, 5]
liste_b = [10, 20, 30, 40, 50]

def combinaison(liste_a, liste_b):
    paires = zip(liste_a, liste_b)
    somme = list(map(lambda x: x[0] + x[1], paires))
    return (somme)

print("\n  ->>> Liste A :")
print(liste_a)

print("\n  ->>> Liste B :")
print(liste_b)

print("\n  ->>> Somme des paires :")
print(combinaison(liste_a, liste_b))