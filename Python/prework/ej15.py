#Ejercicio 15 conversor tiempo de minutos a horas y minutos
minutos_totales = int(input("Introduce el número de minutos: "))

horas = minutos_totales // 60 
minutos = minutos_totales % 60 

print(f"{minutos_totales} minutos son {horas} horas y {minutos} minutos.")

