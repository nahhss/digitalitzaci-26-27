capital_pais = {"Espanya": "Madrid", "França": "París", "Itàlia": "Roma"}
pais="Itàlia"

if pais in capital_pais.keys():
    print(f"La capital de {pais} és {capital_pais[pais]}.")
else:
    print(f"{pais} no està dins del diccionari.")
