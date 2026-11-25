# Troba el valor més gran i el més petit dins d’una llista.
list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]

maxim = None
minim = None

for x in list_num:
    if maxim == None or x > maxim:
        maxim = x

    if minim == None or x < minim:
        minim = x

print("Valor màxim:", maxim)
print("Valor mínim:", minim)