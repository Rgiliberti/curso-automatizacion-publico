# Clase 2 - Actividad 1: datos personales
# Pide nombre, edad y profesión, y muestra un mensaje personalizado.

nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))
profesion = input("¿Cuál es tu profesión? ")

print(f"Hola {nombre}, tenés {edad} años y trabajás como {profesion}.")

if edad >= 18:
    print("Podés postularte en TalentoLab.")
else:
    print("Todavía no tenés la edad para trabajar en TalentoLab.")
