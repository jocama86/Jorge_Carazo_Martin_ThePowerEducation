#Ejercicio 17 -> Conversor millas a km
millas = float(input("Introduce la distancia en millas: "))

factor_conversion = 1.60934

kilometros = millas * factor_conversion

print(f"{millas} millas son {kilometros:.2f} kilómetros.")