#Ejercicio 8 -> Cálculo del indice de masa corporal (IMC)
peso = float(input("Introduce el peso en kilogramos: "))

altura = float(input("Introduce tu altura: "))

imc = peso / (altura ** 2)

print(f"Tu indice de masa es {imc}")