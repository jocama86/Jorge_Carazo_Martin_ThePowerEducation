#Ejercicio -> Contador de vocales

palabra_que_queremos_contar = input("Introduce una palabra: ")

vocales = "aeiouAEIOU"

contador_aux = 0

for letra in palabra_que_queremos_contar:
  if letra in vocales:
    contador_aux += 1

print(contador_aux)