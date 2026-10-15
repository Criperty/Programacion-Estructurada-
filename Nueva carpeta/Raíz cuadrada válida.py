import math

try:
    numero = float(input("Ingresa un número: "))
    resultado = math.sqrt(numero)
    print("La raíz cuadrada es:", resultado)
except ValueError:
    print("Error: no se puede calcular la raíz cuadrada de un número negativo.")