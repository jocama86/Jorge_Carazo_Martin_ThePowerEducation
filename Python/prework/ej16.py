#Ejercicio 16 -> Contador de numeros pares e impares de una lista intrudoducida por el usuario
numeros = input("Introduce una lista de números separados por comas: ")

lista_numeros = [int(num) for num in numeros.split(",")]

pares = 0
impares = 0

for num in lista_numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")