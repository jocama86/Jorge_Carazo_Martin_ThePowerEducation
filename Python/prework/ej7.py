# Ejercicio 7 -> calculadora que permita al usuario hacer operaciones aritmeticas a su eleccion

print("Selecciona la operación a realizar de las siguientes opciones.")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion_escogida = input("Introduce la operación a realizar (1 / 2 / 3 / 4): ")

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if opcion_escogida =='1':
  resultado = num1 + num2
  print(f"El resultado es: {resultado}")
elif opcion_escogida =='2':
  resultado = num1 - num2
  print(f"El resultado es: {resultado}")
elif opcion_escogida =='3':
  resultado = num1 * num2
  print(f"El resultado es: {resultado}")
elif opcion_escogida =='4':
  if num2!= 0:
    resultado = num1 / num2
    print(f"El resultado es: {resultado}")
  else:
    print("Error no se puede dividir por cero.")
else:
  print("Opcion invalida. Selecciona una operació correcta.")