import math

# Numerador y denominador
numerador = (3 * (5**2)) + (4 * (17**20) - 2)
denominador = (9 - 3) * (4 + 2) * 3

# Primera parte
parte1 = (numerador / denominador) * (3 + 2)

# Segunda parte (con resta, no división)
parte2 = math.sqrt(81 * (2 + 3) * (15 - 7)) - 7

# Resultado final
resultado = parte1 + parte2

print("Resultado:", resultado)
