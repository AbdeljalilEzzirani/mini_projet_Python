texte = "ana machii ana wakha ana raah howa ana mais ana dima machii ana hit ana dima howa ana"

print ("\n -->> texte before changement de mot :", texte)

def func_replace(texte):
    text_result = texte.replace("ana", "howa", -1)
    return text_result

text_result = func_replace(texte)
print ("\n -->> texte after changement de mot :", text_result)