try:
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))
    resultado = numero1 / numero2
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.")
except ValueError:
    print("Error: debes ingresar números válidos.")