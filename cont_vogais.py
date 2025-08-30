# 🔹 2. Contar vogais

# Escreva um programa que receba uma string e
# conte quantas vogais (a, e, i, o, u) existem nela.

# Exemplo:
# "programação" → 5 vogais

word = 'programação'

vogais = ['a', 'e', 'i', 'o', 'u', 'ã', 'á', 'à', 'â']
contagem = 0

for i in word.lower():
    for x in vogais:
        if x == i:
            contagem += 1
            
print(contagem)
