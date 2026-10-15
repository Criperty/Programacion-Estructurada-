try:
    numero = int(input("Ingresa un número entero: "))
except ValueError:
    print("Error: debes ingresar un número entero válido.")
else:
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")