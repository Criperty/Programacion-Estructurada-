def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    return edad

try:
    edad = int(input("Ingresa tu edad: "))
    validar_edad(edad)
    print("Edad válida:", edad)
except ValueError as e:
    print("Error:", e)