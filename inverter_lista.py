# 1. Inverter uma lista

# Dada uma lista [1, 2, 3, 4, 5], crie um algoritmo
# que retorne [5, 4, 3, 2, 1] sem usar reverse() ou [::-1].

lista = [1, 2, 3, 4, 5]
new = []

last_index = (len(lista)) - 1

while last_index >= 0:
    new.append(lista[last_index])
    last_index -= 1
    
print(new)