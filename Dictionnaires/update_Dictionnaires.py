# Challenge : Mise à Jour de Dictionnaires
# Objectif : Fusionner plusieurs dictionnaires en un seul.
# Travail à faire :
# Utilisez update() pour fusionner trois dictionnaires différents.
# Affichez le dictionnaire final avec toutes les clés et valeurs combinées.

dictionary0 = {'ahmed': 2, "speed": 13, "binchii": 4, "hello": 5}
dictionary1 = {"vive": 12, "low": 31, "state": 20, "broos": 10}
dictionary2 = {"quel": 22, "prince": 32, "loop": 30, "make": 15}


# def update_dic(dictionary0, dictionary1, dictionary2):
#     i = 0
#     j = len(dictionary0) + len(dictionary1) + len(dictionary2)
#     while i < j:
#         k = 0
#         dictionary0.update(dictionary1)
#         dictionary0.update(dictionary2)

#     # new_dict = {**dictionary0, **dictionary1, **dictionary2}
#     return new_dict

# print (update_dic(dictionary0, dictionary1, dictionary2))

def combine(*arg):
    combine_dict={}
    for dic in arg:
        if type(dic)==dict:
            combine_dict.update(dic)
    return combine_dict

print(combine(dictionary0, dictionary1, dictionary2))
