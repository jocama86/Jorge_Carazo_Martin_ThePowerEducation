#Ejercicio 9 -> Conversor de divisas

dolares = float(input("Introduce la cantidad en dolares: "))

tasa_de_conversion = 0.85

euros = dolares * tasa_de_conversion

print(f"{dolares} dólares son: {euros:.2f} euros.")