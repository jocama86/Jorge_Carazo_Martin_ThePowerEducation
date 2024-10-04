#Ejercicio 14 -> Calculadora de descuento del 20 %
precio_original = float(input("Introduce el precio original del artículo: "))

descuento = precio_original * 0.20

precio_final = precio_original - descuento

print(f"El precio final después del descuento es: {precio_final:.2f} euros")

#lo interesante seria declarar el "magic number del 0.2" como una variable que se pueda introducir para que se pueda calcular cualquier tipo de descuento