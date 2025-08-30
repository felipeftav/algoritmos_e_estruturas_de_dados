fibonacci = [0, 1]

while len(fibonacci) <= 10:
    x = fibonacci[-1]
    y = fibonacci[-2]
    soma = x + y
    fibonacci.append(soma)
    
print(fibonacci)
