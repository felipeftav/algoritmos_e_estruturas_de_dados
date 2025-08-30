# Faça um Programa que peça o raio
# de um círculo, calcule e mostre sua área.

# Formula : A = πr²

import math

pi = math.pi

user_prompt = float(
    input("Insira um numero de um Raio de um circulo: ")
)

A = pi * (user_prompt ** 2)

print(A)