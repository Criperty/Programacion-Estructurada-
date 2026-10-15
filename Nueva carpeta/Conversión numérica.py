try:
    numero = int(input("Ingresa un número entero: "))
    print("Número ingresado:", numero)
except ValueError:
    print("Error: el valor ingresado no es un número entero válido.")