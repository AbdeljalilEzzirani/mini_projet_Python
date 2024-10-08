from functools import reduce

liste_nombres = [1, 2, 3, 4, 5]

def produitcomutatif(liste_nombre):
    produit_cumulatif = reduce(lambda x, y: x * y, liste_nombres)
    return (produit_cumulatif)

print("\n  ->>> Liste de nombres :")
print(liste_nombres)

print("\n  ->>> Produit cumulatif :")
print(produitcomutatif(liste_nombres))
