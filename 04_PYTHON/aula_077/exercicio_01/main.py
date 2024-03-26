print("\n\n")

import math
import random

original = -10
n_abs = abs(original)
aleatorio = random.randint(1, 5)

print("=== Funções dos Inteiros ===")

print()

print("Inteiro 'original': (", original, ")", sep="")
print("Inteiro 'módulo': (", n_abs, ")", sep="")

print()
print("Número inteiro aleatório 'entre 1 e 5': (", aleatorio, ")", sep="")

print()

print("=== Funções dos Floats ===")

print()

float_original = 3.567
arredondado = round(float_original)
arredondado_1 = round(float_original, 1)
arredondado_2 = round(float_original, 2)
floor = math.floor(float_original)
ceil = math.ceil(float_original)



print("Float 'original': (", float_original, ")", sep="")

print()

print("Float 'arredondado': (", arredondado, ")", sep="")
print("Float 'arredondado para 1 casa decimal': (", arredondado_1, ")", sep="")
print("Float 'arredondado para 2 casas decimais': (", arredondado_2, ")", sep="")

print()

print("Float 'arredondado para cima': (", ceil, ")", sep="")
print("Float 'arredondado para baixo': (", floor, ")", sep="")



print("\n\n")