# Clase 2 - Actividad 2: los primeros 10 números pares
# Usa un bucle while, un condicional y un contador.

numero = 1
contador = 0

while contador < 10:
    if numero % 2 == 0:
        print(numero)
        contador += 1
    numero += 1
