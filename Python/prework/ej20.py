#Ejercicio 20 -> Crea un programa que sume todos los numeros de una lista ingresada por el usuario
numeros = input("Introduce una lista de números separados por comas: ")

lista_numeros = [float(num) for num in numeros.split(",")]

suma = sum(lista_numeros)

print(f"La suma de los números en la lista es: {suma}")

#habría que controlar que no se pudiesen meter comas sueltas al final por ejemplo. Lo dejo asi por simplificar.