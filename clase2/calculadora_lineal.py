# Clase 2 - Calculadora lineal (sin funciones)
# En la Clase 3 se refactoriza en funciones y en la Clase 4 se le agregan tests.

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

print("\nSeleccione una operación:")
print("1 - Sumar")
print("2 - Restar")
print("3 - Multiplicar")
print("4 - Dividir")

opcion = input("Ingrese una opción (1-4): ")

if opcion == "1":
    print(f"El resultado es: {numero1 + numero2}")
elif opcion == "2":
    print(f"El resultado es: {numero1 - numero2}")
elif opcion == "3":
    print(f"El resultado es: {numero1 * numero2}")
elif opcion == "4":
    if numero2 == 0:
        print("Error: no se puede dividir por cero.")
    else:
        print(f"El resultado es: {numero1 / numero2}")
else:
    print("Error: opción inválida.")
