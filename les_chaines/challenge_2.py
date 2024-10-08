noms = ["  one ", "two    ", "         three", "     foure        "]

def normalisation(noms):
    i = 0
    length = len(noms)
    normalisation = [None] * length
    maj_noms = [None] * length
    while i < length:
        nom = noms[i]
        normalisation[i] = nom.strip(' ')
        maj_noms[i] = normalisation[i].upper()
        i += 1
    return normalisation, maj_noms

normalisation, maj_noms = normalisation(noms)
# print ("\n\n --->>>>here", normalisation(noms))
print ("\n -->  Normaliser une liste de noms en supprimant les espaces superflus :")
print (normalisation)

print ("\n  --> Convertissez les noms en majuscules :")
print (maj_noms)