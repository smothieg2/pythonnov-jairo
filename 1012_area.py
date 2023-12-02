A, B, C = map(float, input().split())
pi = 3.14159
# Calcular áreas
area_triangulo = (A * C) / 2
area_circulo = pi * (C ** 2)
area_trapecio = ((A + B) * C) / 2
area_cuadrado = B ** 2
area_rectangulo = A * B


print("TRIANGULO: {:.3f}".format(area_triangulo))
print("CIRCULO: {:.3f}".format(area_circulo))
print("TRAPEZIO: {:.3f}".format(area_trapecio))
print("QUADRADO: {:.3f}".format(area_cuadrado))
print("RETANGULO: {:.3f}".format(area_rectangulo))