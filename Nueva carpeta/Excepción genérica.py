try:
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))
    resultado = numero1 / numero2
    print("Resultado:", resultado)
except Exception as e:
    print("Tipo de error:", type(e))
    print("Mensaje del error:", str(e))