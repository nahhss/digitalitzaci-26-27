#Partint del mateix cotxe: afegeix "color": "vermell", canvia "any" a 2020 i elimina "model" amb pop(). 
#Mostra el valor eliminat i el diccionari final.

d={"marca": "Seat", "model": "Ibiza", "any": 2019, 'color': 'vermell'}

print(d)
d["any"] = 2020
model=d.pop("model")
print(model)
print(d)