# Función para sumar
def sumar(a, b):
    return a + b


# Función para restar
def restar(a, b):
    return a - b


# Función para multiplicar
def multiplicar(a, b):
    return a * b


# Función para dividir
def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


# Programa principal
def calculadora():
    try:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Error: debe ingresar números válidos.")
        return

    print("\nSeleccione una operación:")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")

    opcion = input("Ingrese una opción (1-4): ")

    try:
        if opcion == "1":
            resultado = sumar(numero1, numero2)

        elif opcion == "2":
            resultado = restar(numero1, numero2)

        elif opcion == "3":
            resultado = multiplicar(numero1, numero2)

        elif opcion == "4":
            resultado = dividir(numero1, numero2)

        else:
            print("Error: opción inválida.")
            return

        print(f"El resultado es: {resultado}")

    except ValueError as error:
        print(f"Error: {error}")


# Solo se ejecuta al correr este archivo, no al importarlo desde los tests
if __name__ == "__main__":
    calculadora()
