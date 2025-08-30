pares = []
n = 0

def checar_par(x):
    if x % 2 == 0:
        return True
    
while len(pares) <= 10:
    if checar_par(n):
        pares.append(n)
        n += 2        
        
print(pares)