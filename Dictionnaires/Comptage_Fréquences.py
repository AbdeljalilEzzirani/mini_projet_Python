# Challenge : Comptage de Fréquences
# Objectif : Créer un dictionnaire de fréquences à partir d'une liste de mots.
# Travail à faire :
# Pour chaque mot dans une liste, utilisez get() pour mettre à jour son compteur.
# Affichez le dictionnaire des fréquences des mots.



# ***************** dictionary vers une liste

# dictionary = {"ahmed": 10, "hala": 12, "said": 14, "pedro":16}

# def Comptage_Fréquences(dictionary):
#     new_dict = []
#     lista = list(dictionary.keys())
#     i = 0
#     while i < len(lista):
#         name = lista[i]
#         key = dictionary.get(name)
#         new_dict.append(key)
#         i += 1
#     return new_dict

# print ("\n\n -->>>>>   result is :", Comptage_Fréquences(dictionary))


# ***************** liste vers une dictionary # give number of name

liste = ["ahmed", "hala", "said", "pedro", "ahmed", "hala", "hala", "said", "said", "said", "pedro", "pedro", "pedro", "pedro"]

def Comptage_Fréquences(dictionary):
    return_dict = {}
    i = 0
    while i < len(liste):
        name = liste[i]
        return_dict[name] = return_dict.get(name, 0) + 1
        i += 1
    return return_dict

print ("\n\n -->>>>>   result is :", Comptage_Fréquences(liste))
