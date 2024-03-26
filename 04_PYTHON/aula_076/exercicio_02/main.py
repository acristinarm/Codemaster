print("\n\n")

#Importações
import math

a = 27

raiz = a ** (1/3) #utilizando a potência faço a raiz cúbica, se mudar o denominador consigo outras raizes

raiz_2 = math.sqrt(a) #com o import tenho já a fórmula para a raiz quadrada

print(raiz)
print(raiz_2)

seno = math.sin( math.radians(90)) #exemplo com seno
print(seno)

b = 8
c = 3
div = 8 / 3

div_1 = round(div, 1) #resultado arredondado a 1 casa décimal
div_2 = round(div, 2) #resultado arredondado a 2 casas décimais
div_3 = round(div, 3) #resultado arredondado a 3 casas décimais

print(div_1)
print(div_2)
print(div_3)

div_floor = math.floor(div) #arredonda para baixo "chão"
div_ceil = math.ceil(div) #arredonda para cima "telhado"

import random

aleatorio = random.randint(-5, 5)

print("Aleatório = (", aleatorio, ")", sep="")

n = -10
n_abs = abs(10) #deste modo tenho o módulo do nº negativo

print("Inteiro 'módulo': (", n_abs, ")", sep="")


print("\n\n")