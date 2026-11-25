# Pregunta a l’usuari un número i comprova si està dins d’una llista.
list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]

num = int(input("Introdueix un número: "))

if num in list_num:
    print("El número està dins de la llista")
else:
    print("El número no està dins de la llista")
