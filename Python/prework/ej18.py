#Ejercicio 18 -> Crea un programa que cuente el numero de palabras en una frase.
frase = input("Introduce una frase: ")

palabras = frase.split()

cantidad_palabras = len(palabras)

print(f"La cantidad de palabras en la frase es: {cantidad_palabras}")