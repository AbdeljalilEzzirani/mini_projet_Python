email = ["hello@gmail.com", "hello@hotmail.com", "hello@mail.com"]

def domain(email):

    i = 0
    length = len(email)
    domains = [None] * length
    noms = [None] * length
    while i < length:
        mail = email[i]
        nom_utilisateur, domain = mail.split('@')
        noms[i] = nom_utilisateur
        domains[i] = domain
        i += 1
    domain_unique = set(domains)

    return domain_unique, noms, domains

domain_unique, noms, domains = domain(email)

print ("\n #*# Une liste des domaines extraits :")
print("les noms --> ", noms)
print("les domains --> ", domains)

print ("\n #*# Affichez la liste des domaines uniques :")
print (domain_unique)
