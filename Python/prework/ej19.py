#Ejercicio 19 -> Escribe un programa que determine si un año es bisiesto o no.
fecha = int(input("Introduce un año: "))

# Verificar si el año es bisiesto
if (fecha % 4 == 0 and fecha % 100 != 0) or (fecha % 400 == 0):
    print(f"{fecha} es un año bisiesto.")
else:
    print(f"{fecha} no es un año bisiesto.")