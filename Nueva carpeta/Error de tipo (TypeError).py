try:
    edad = int(input("Ingresa tu edad: "))
    mensaje = "Edad: " + edad
    print(mensaje)
except TypeError:
    print("Error: no se puede concatenar texto con un número entero.")
except ValueError:
    print("Error: debes ingresar una edad válida.")