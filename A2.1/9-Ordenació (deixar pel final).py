list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
list_ordenada = []

while len(list_num) > 0:
    minim = min(list_num)
    list_ordenada.append(minim)
    list_num.remove(minim)

print(list_ordenada)