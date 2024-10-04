#ejercicio 5 -> Calculadora de todos los numeros pares del 1 al 100, por simplificar lo hago hasta el 8

suma_de_pares = 0

for numero in range(1, 8):
  if(numero % 2 ==0):
    suma_de_pares += numero


print(suma_de_pares)