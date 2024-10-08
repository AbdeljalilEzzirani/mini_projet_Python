date = ["11/02/2002", "21/03/2003", "31/04/2004"]

def date_func(date):
    i = 0
    length = len(date)
    conversion = [None] * length
    while i < length:
        day, month, year = date[i].split('/')
        conversion[i] = '-'.join([year, month, day])
        i += 1
    return conversion
conversion = date_func(date)
print (" ---->   Conversion de Format de Date :")
print (conversion)
