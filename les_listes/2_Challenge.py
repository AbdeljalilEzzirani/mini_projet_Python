liste_number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

liste_impaire = []
i = 0
while i < len(liste_number):
    number = int(liste_number[i])
    if number % 2 != 0:
            liste_impaire.append(liste_number[i])
    i += 1

print ("\n  ->>> before change the liste :")
print (liste_number)
print ("\n  ->>> after change the liste :")
print (liste_impaire)