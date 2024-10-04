#Ejercicio 10 -> Determinar el dia de la semana

numero_dia = int(input("Introduce un número (1 para lunes, 2 para martes, etc.): "))

if numero_dia == 1:
    dia = "Lunes"
elif numero_dia == 2:
    dia = "Martes"
elif numero_dia == 3:
    dia = "Miércoles"
elif numero_dia == 4:
    dia = "Jueves"
elif numero_dia == 5:
    dia = "Viernes"
elif numero_dia == 6:
    dia = "Sábado"
elif numero_dia == 7:
    dia = "Domingo"
else:
    dia = "Número inválido. Por favor, introduce un número del 1 al 7."

print(f"El día correspondiente es: {dia}")